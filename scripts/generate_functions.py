import os
import re

from clickhouse_connect import get_client
from jinja2 import Template

url = os.environ.get("CLICKHOUSE_URL", "clickhouse://default:default@localhost:8123")
path = os.environ.get("CLICKHOUSE_FUNCTIONS_PATH", "src/pyclickhouse/functions.py")
query = "select * from system.functions where empty(alias_to) order by name"


def _get_args(syntax: str) -> tuple[list[str], list[str]]:
    required = []
    optional = []

    # Extract everything inside the main parentheses
    if inner_match := re.search(r"\((.*?)\)", syntax):
        inner_content = inner_match.group(1)
        parts = inner_content.split("[", 1)
        required_str = parts[0]
        optional_str = parts[1] if len(parts) > 1 else ""

        # 3. Define a regex to find arguments (including those with default values)
        # This looks for: word + optional (space + = + space + value)
        arg_pattern = r"[\w_]+(?:\s*=\s*[^,\]]+)?"

        # 4. Extract and clean the lists
        required = [
            a.strip() for a in re.findall(arg_pattern, required_str) if a.strip()
        ]
        optional = [
            a.strip() for a in re.findall(arg_pattern, optional_str) if a.strip()
        ]
    required = [_clean_name(var) for var in required]
    optional = [_clean_name(var) for var in optional]

    return required, optional


def _clean(item: str) -> str:
    # for documentation
    item = item.replace(":::", "")
    # for warnings
    item = item.replace("\\`", "\\\\`")
    # for reference urls
    item = item.replace("/sql-reference/", "https://clickhouse.com/docs/sql-reference/")
    return item


reserved_names = ["if", "in", "and", "not", "except", "lambda", "from", "or", "else"]


def _clean_name(name: str) -> str:
    if name in reserved_names:
        return f"{name}_"
    return name


exclude = [
    "arrayShingles",
    "pointInEllipses",
    "uniqThetaIntersect",
    "uniqThetaNot",
    "uniqThetaUnion",
]


def generate() -> None:
    client = get_client(dsn=url)
    rows = client.query(query)
    items = list(rows.named_results())

    functions = []

    for item in items:
        name = item.get("name")
        if name and isinstance(name, str):
            if name.startswith("_"):
                continue
            if name in exclude:
                continue
            safe_name = _clean_name(name)
        syntax = item["syntax"].strip()
        required, optional = _get_args(syntax)
        combined = [*required, *optional]
        if len(set(combined)) > len(combined):
            continue
        args = []
        for arg in required:
            if len(arg.split("=")) > 1:
                arg = arg.split("=")
                args.append(f"{arg[0]}: {arg[1]}")
            else:
                args.append(f"{arg}: Any")
        for arg in optional:
            if len(arg.split("=")) > 1:
                arg = arg.split("=")
                args.append(f"{arg[0]}: Any | None = {arg[1]}")
            else:
                args.append(f"{arg}: Any | None = None")
        if not args and not syntax:
            args.append("*args: Any")
        fn = {
            "name": name,
            "safe_name": safe_name,
            "args": ", ".join(args),
            "syntax": syntax,
            "required": required,
            "optional": optional,
            "arguments": _clean(item["arguments"]),
            "returns": _clean(item["returned_value"]),
        }
        functions.append(fn)

    with open("scripts/functions.py.j2") as tp:
        template = Template(tp.read())

    generated = template.render(functions=functions)

    with open(path, "w") as fp:
        fp.write(generated)

    print(f"Created {path} with {len(functions)} functions")


if __name__ == "__main__":
    generate()
