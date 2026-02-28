import re


def pascal_to_snake(name: str) -> str:
    """Converts a PascalCase string to snake_case."""
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()
