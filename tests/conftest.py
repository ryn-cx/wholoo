# TODO: Validate
import pytest
from get_around import build_client_automatically

from wholoo import Wholoo


@pytest.fixture(scope="session")
def client() -> Wholoo:
    return Wholoo(build_client_automatically())
