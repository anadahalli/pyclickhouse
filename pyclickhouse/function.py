from typing import Any, Callable

from .expression import Expression


class Function:
    def __getattr__(self, name: str) -> Callable[..., Expression]:
        def wrapper(*args: Any) -> Expression:
            params = ", ".join(map(str, args))
            value = f's"{name}({params})"'
            return Expression(value)

        return wrapper


F = Function()
