import re
import sys
from typing import Any

from loguru import logger

# logging
logger.bind(name="pyclickhouse")
logger.configure(
    handlers=[
        {
            "sink": sys.stdout,
            "colorize": True,
            "format": "<level>{level: <8}</level> <green>{time}</green> {message}",
        },
    ],
)


def pascal_to_snake(name: str) -> str:
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


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
