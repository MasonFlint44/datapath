import subprocess
import tempfile
from textwrap import dedent

import pytest

from datapath import Path


def test_path_call(data: dict):
    assert Path.foo.bar[0].baz(data) == 1
    assert Path.foo.bar[1].baz(data) == 2


def test_path_call_raises_key_error(data: dict):
    with pytest.raises(KeyError):
        Path.foo.bar[3].baz(data)


def test_path_call_with_default_value(data: dict):
    assert Path.foo.bar[3].baz(data, default=None) is None
    assert Path.foo.bar[3].baz(data, default=42) == 42


def test_path_call_returns_any(data: dict):
    # Python code to test using dedent for better formatting
    code = dedent(
        f"""
        from datapath import Path

        data = {data}

        path = Path.foo.bar[0].baz(data)

        reveal_type(path)
        """
    )

    # Write the code to a temporary file
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".py") as tmp:
        tmp.write(code)
        tmp_file_name = tmp.name

    # Run MyPy on the temporary file
    result = subprocess.run(
        ["mypy", "--show-error-codes", tmp_file_name],
        text=True,
        capture_output=True,
        check=True,
    )

    # Check for specific output indicating the correct type
    expected_output = 'note: Revealed type is "Any"'
    assert (
        expected_output in result.stdout
    ), f"Type check failed, output was:\n{result.stdout}"


def test_path_call_returns_default_type(data: dict):
    # Python code to test using dedent for better formatting
    code = dedent(
        f"""
        from datapath import Path

        data = {data}

        path = Path.foo.bar[0].baz(data, default=42)

        reveal_type(path)
        """
    )

    # Write the code to a temporary file
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".py") as tmp:
        tmp.write(code)
        tmp_file_name = tmp.name

    # Run MyPy on the temporary file
    result = subprocess.run(
        ["mypy", "--show-error-codes", tmp_file_name],
        text=True,
        capture_output=True,
        check=True,
    )

    # Check for specific output indicating the correct type
    expected_output = 'note: Revealed type is "builtins.int"'
    assert (
        expected_output in result.stdout
    ), f"Type check failed, output was:\n{result.stdout}"


def test_path_call_returns_specific_type(data: dict):
    # Python code to test using dedent for better formatting
    code = dedent(
        f"""
        from datapath import Path

        data = {data}

        path = Path.foo.bar[0].baz(data, type_=int)

        reveal_type(path)
        """
    )

    # Write the code to a temporary file
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".py") as tmp:
        tmp.write(code)
        tmp_file_name = tmp.name

    # Run MyPy on the temporary file
    result = subprocess.run(
        ["mypy", "--show-error-codes", tmp_file_name],
        text=True,
        capture_output=True,
        check=True,
    )

    # Check for specific output indicating the correct type
    expected_output = 'note: Revealed type is "builtins.int"'
    assert (
        expected_output in result.stdout
    ), f"Type check failed, output was:\n{result.stdout}"


def test_path_call_with_default_value_returns_specific_type(data: dict):
    # Python code to test using dedent for better formatting
    code = dedent(
        f"""
        from datapath import Path

        data = {data}

        path = Path.foo.bar[3].baz(data, default="asdf", type_=int)

        reveal_type(path)
        """
    )

    # Write the code to a temporary file
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".py") as tmp:
        tmp.write(code)
        tmp_file_name = tmp.name

    # Run MyPy on the temporary file
    result = subprocess.run(
        ["mypy", "--show-error-codes", tmp_file_name],
        text=True,
        capture_output=True,
        check=True,
    )

    # Check for specific output indicating the correct type
    expected_output = 'note: Revealed type is "builtins.int"'
    assert (
        expected_output in result.stdout
    ), f"Type check failed, output was:\n{result.stdout}"


def test_path_call_returns_optional_type(data: dict):
    # Python code to test using dedent for better formatting
    code = dedent(
        f"""
        from datapath import Path

        data = {data}

        path = Path.foo.bar[3].baz(data, optional=int)

        reveal_type(path)
        """
    )

    # Write the code to a temporary file
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".py") as tmp:
        tmp.write(code)
        tmp_file_name = tmp.name

    # Run MyPy on the temporary file
    result = subprocess.run(
        ["mypy", "--show-error-codes", tmp_file_name],
        text=True,
        capture_output=True,
        check=True,
    )

    # Check for specific output indicating the correct type
    expected_output = 'note: Revealed type is "Union[builtins.int, None]"'
    assert (
        expected_output in result.stdout
    ), f"Type check failed, output was:\n{result.stdout}"


def test_path_call_returns_default_none_with_optional(data: dict):
    assert Path.foo.bar[3].baz(data, optional=int) is None


def test_path_call_checks_type(data: dict):
    with pytest.raises(TypeError):
        Path.foo.bar[0].baz(data, type_=str)


def test_path_call_checks_type_with_optional(data: dict):
    with pytest.raises(TypeError):
        Path.foo.bar[0].baz(data, optional=str)


def test_path_call_does_not_check_type(data: dict):
    assert Path.foo.bar[0].baz(data, type_=str, check_type=False) == 1  # type: ignore
    assert Path.foo.bar[0].baz(data, optional=str, check_type=False) == 1  # type: ignore


def test_path_call_returns_none_with_optional_when_value_is_none(data: dict):
    assert Path.foo.bar[2].baz(data, optional=int) is None


def test_path_call_raises_error_with_type__when_value_is_none(data: dict):
    with pytest.raises(TypeError):
        Path.foo.bar[2].baz(data, type_=int)
