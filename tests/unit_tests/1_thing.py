import pytest


class ThingTests:
    """
    Note that the test clases must end with `Tests` and
    the test functions must begin with `test_`.
    Test files are recommended to start with a number,
    so testing functionality can be ordered
    """

    def test_thing_works_good(self):
        assert True == True

    def test_thing_errors_good(self):
        with pytest.raises(ValueError, match="Oh no!"):
            raise ValueError("Oh no!")
