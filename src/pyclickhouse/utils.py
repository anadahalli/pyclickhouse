import re
import sys
from typing import Any

from loguru import logger
from pydantic import BaseModel, create_model

from pyclickhouse.types import get_python_type_from_ch_string

# logging
logger.configure(
    handlers=[
        {
            "sink": sys.stdout,
            "colorize": True,
            "format": "<level>{level: <8}</level> <green>{time}</green> {message}",
        },
    ],
)
logger.bind(name="pyclickhouse")
logger.disable(name="pyclickhouse")


def pascal_to_snake(name: str) -> str:
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def escape(value: Any) -> str:
    if isinstance(value, str):
        return f"'{value}'"
    return value


def comma_join(
    data: dict[str, Any],
    *,
    prefix: str | None = None,
    stringify: bool = False,
) -> str:
    if stringify:
        joined = ", ".join(f"{k} = {str(v)}" for k, v in data.items())
    else:
        joined = ", ".join(f"{k} = {v}" for k, v in data.items())

    if prefix:
        return f"{prefix} {joined}"
    return joined


def clean_query_param_types(text: str) -> str:
    return re.sub(pattern=r"\{([^:]+):[^}]+\}", repl=r"{\1}", string=text)


def create_model_from_sql(name: str, columns: list[dict[str, str]]) -> type[BaseModel]:
    fields: dict[str, Any] = {}
    for col in columns:
        fields[col["name"]] = get_python_type_from_ch_string(str(col["type"]))
    return create_model(name, **fields)
