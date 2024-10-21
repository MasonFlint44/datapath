import pytest


@pytest.fixture
def data():
    return {
        "foo": {
            "bar": [
                {"baz": 1},
                {"baz": 2},
                {"baz": None},
            ]
        }
    }
