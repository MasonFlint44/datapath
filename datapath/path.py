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

    def __call__(
        self, data, *, default=unassigned, type_=None, optional=None, check_type=True
    ):
        # Navigate through the data according to the path
        result = data
        for step in self.path:
            try:
                # Try to access the key or index
                result = result[step]
            except (KeyError, IndexError) as e:
                # Return the default value if it is set
                if default is not unassigned:
                    return default
                # Return None if the optional type is set
                if optional is not None:
                    return None
                # Raise an error if no default value is set
                raise KeyError(f"Invalid path or index '{step}' at {result}") from e

        # Check the type of the result
        if check_type:
            if type_ is not None and not isinstance(result, type_):
                raise TypeError(f"Expected type {type_}, got {type(result)}")
            if (
                optional is not None
                and result is not None
                and not isinstance(result, optional)
            ):
                raise TypeError(f"Expected type {optional}, got {type(result)}")

        return result

    def __repr__(self):
        return f"Path({self.path})"
