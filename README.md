# datapath

The `datapath` package offers an intuitive way to access and manipulate nested data structures in Python, making it easier to build clean and readable data pipelines. This package is particularly useful when dealing with complex data types such as nested dictionaries, lists, or combinations thereof. It leverages a class named `Path` to simplify the process of data traversal.

## Features

- **Easy navigation of nested data**: Use simple attribute and item access to traverse nested dictionaries, lists, and other indexable data structures.
- **Flexible data retrieval**: Retrieve data with optional type checking and default values if the path does not exist or leads to an error.
- **Enhanced readability**: Create more readable code by abstracting complex data access into straightforward, path-based retrievals.

## Installation

`datapath` is available on PyPI, so you can install it using using pip:

```bash
pip install datapath
```

## Basic Usage

The `Path` class is the core of the `datapath` package. Here's how you can use it:

### Creating a Path

```python
from datapath import Path

# Create a Path simply by chaining attributes or items
path = Path.data.users[0].name
```

### Accessing Data

Once you've created a path, you can use it to access data in nested structures:

```python
# Given a nested dictionary
data = {
    "data": {
        "users": [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25}
        ]
    }
}

# To retrieve data using the path, simply call the path with the data as an argument.
user_name = Path.data.users[0].name(data)
# Prints 'Alice'
```

## Advanced Usage

### Type Checking and Default Values

The `Path` class allows for more complex operations like type checking and specifying default values if a path does not exist:

#### Using Default Values

If a part of the path doesn't exist, you can specify a default value to return instead of raising an error:

```python
# Returns 'Unknown' if the specified index is out of range
name = Path.data.users[2].name(data, default="Unknown")
print(name)  # Outputs 'Unknown'
```

#### Type Checking

You can enforce the type of the returned value:

```python
# Specify the expected type, returns the value if it matches, raises an error otherwise
age = Path.data.users[0].age(data, type_=int)
print(age) # Outputs 30
```

### Optional Type Specification

You can specify that a return type is optional, which means it will return `None` if the path is not found or the type does not match, rather than raising an error:

```python
# Optional type checking, returns None if not found or type mismatch
profile_pic = Path.data.users[0].profile_picture(data, optional=str)
print(profile_pic)  # Outputs None since 'profile_picture' does not exist
```

## Understanding the Overloads

The `__call__` method of the `Path` class supports several overloads to provide flexibility in how data is accessed:

- **data**: The nested structure to be accessed.
- **default**: If provided, this value is returned when the path leads to an error or does not exist.
- **type_**: Enforces that the returned value matches this type, raising an error if it does not. Also determines the return type of the `__call__` method.
- **optional**: Like `type_`, but returns `None` instead of raising an error when the type does not match or the path does not exist. Also used to determine the return type of the `__call__` method.
- **check_type**: If `True`, the type of the returned value is checked against `type_` or `optional` (default is `True`). If the type does not match, a TypeError is raised. When `False`, no type checking is performed (faster but less safe).

## Conclusion

The `datapath` package simplifies the way you interact with complex data structures. By abstracting the complexity of data traversal into simple path operations, it enables cleaner and more maintainable code in data-heavy applications.
