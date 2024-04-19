import pytest

from datapath import Path


def test_path():
    data = {
        "foo": {
            "bar": [
                {"baz": 1},
                {"baz": 2},
            ]
        }
    }
    assert Path.foo.bar[0].baz(data) == 1
    assert Path.foo.bar[1].baz(data) == 2
