import logging
from uuid import uuid4

import pytest

logger = logging.getLogger(__name__)

# Add global test fixtures to this file
# https://docs.pytest.org/en/latest/how-to/fixtures.html#scope-sharing-fixtures-across-classes-modules-packages-or-session


@pytest.fixture(scope="session")
def test_id():
    test_run_id = str(uuid4())
    logging.warning(f"Using keys with the prefix: {test_run_id}")
    return test_run_id


def pytest_generate_tests(metafunc):
    """
    This function can be used to add dynamic fixtures
    https://docs.pytest.org/en/latest/example/parametrize.html
    """
    pass
