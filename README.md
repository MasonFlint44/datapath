# datapath

![PyPI](https://img.shields.io/pypi/v/datapath?style=for-the-badge) ![PyPI - License](https://img.shields.io/pypi/l/datapath?style=for-the-badge)

Easily navigate nested data structures for building readable data pipelines.

## Use case

Do you ever find yourself writing ugly code to access nested values? Fret no longer!

#### Go from this:
```python
data = {
    "users": {
        "Alice": {
            "profile": {
                "age": 30,
                "email": "alice@example.com"
            }
        },
        "Bob": {
            "profile": {
                "age": 25,
                "email": "bob@example.com"
            }
        }
    }
}

alice_age = data["users"]["Alice"]["profile"]["age"]
alice_email = data["users"]["Alice"]["profile"]["email"]

bob_age = data.get("users", {}).get("Bob", {}).get("profile", {}).get("age", "Unknown")
bob_email = data.get("users", {}).get("Bob", {}).get("profile", {}).get("email", "Unknown")
```

#### To this:
```python
from datapath import Path


alice_age = Path.users.Alice.profile.age(data)
alice_email = Path.users.Alice.profile.email(data)

bob_age= Path.users.Bob.profile.age(data, default="Unknown")
bob_email = Path.users.Bob.profile.email(data, default="Unknown")
```

## Features

- **Easy navigation of nested data**: Use simple attribute and item access to traverse nested dictionaries and lists.
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
print(user_name)    # Prints 'Alice'
```

## Advanced Usage

### Using Default Values

If a part of the path doesn't exist, you can specify a default value to return instead of raising an error:

```python
# Returns 'Unknown' if the specified index is out of range
name = Path.data.users[2].name(data, default="Unknown")
print(name)  # Prints 'Unknown'
```

### Type Checking

You can enforce the type of the returned value:

```python
# Specify the expected type, returns the value if it matches, raises a TypeError otherwise
age = Path.data.users[0].age(data, type_=int)
print(age) # Prints 30
```

> Note: Type enforcement can be disabled by setting `check_type` to False. `type_` and `optional` can still be used to define type hints for your data when `check_type` is False.

#### Optional Type Specification

You can specify that a return type is optional, which means it will return `None` if the path is not found or the type does not match, rather than raising an error:

```python
# Optional type checking, returns None if not found or type mismatch
birthday = Path.data.users[0].birthday(data, optional=str)
print(birthday)  # Prints None since 'birthday' does not exist
```

## Understanding the Arguments

The `__call__` method of the `Path` class supports several arguments that adjust the behavior to be used when accessing values:

- **data**: The nested structure to be accessed.
- **default**: If provided, this value is returned when the path leads to an error or does not exist.
- **type_**: Enforces that the returned value matches this type, raising a TypeError if it does not.
- **optional**: Like `type_`, but returns `None` instead of raising a KeyError when the path does not exist. 
- **check_type**: If `True`, the type of the returned value is checked against `type_` or `optional` (default is `True`). If the type does not match, a TypeError is raised. When `False`, no type checking is performed (faster but less safe).
