import pytest

from {{cookiecutter.project_slug}}.fib import fib

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_known_values(test_input: int, expected: int):
    assert fib(test_input) == expected
