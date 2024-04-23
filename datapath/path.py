from typing import Any, TypeVar, overload

T = TypeVar("T")

unassigned = object()


class Path:
    def __init__(self, path: list[str | int] | None = None) -> None:
        if path is None:
            path = []
        self.path = path

    def __getattr__(self, name) -> "Path":
        return Path(self.path + [name])

    def __getitem__(self, index) -> "Path":
        return Path(self.path + [index])

    @overload
    def __call__(self, data) -> Any: ...

    @overload
    def __call__(self, data, *, type_: type[T]) -> T: ...

    @overload
    def __call__(self, data, *, optional: type[T]) -> T | None: ...

    @overload
    def __call__(self, data, *, default: T) -> T: ...

    @overload
    def __call__(self, data, *, default, type_: type[T]) -> T: ...

    @overload
    def __call__(self, data, *, default, optional: type[T]) -> T | None: ...

    def __call__(self, data, *, default=unassigned, type_=Any, optional=None):
        # Navigate through the data according to the path
        result = data
        for step in self.path:
            try:
                result = result[step]
            except (KeyError, IndexError, TypeError) as e:
                if default is not unassigned:
                    return default
                raise KeyError(f"Invalid path or index '{step}' at {result}") from e
        return result

    def __repr__(self):
        return f"Path({self.path})"
