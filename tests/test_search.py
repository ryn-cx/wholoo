from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from wholoo import Wholoo
    from wholoo.search import Search
    from wholoo.search.models import SearchModel


class TestData(BaseModel):
    query: str
    name: str
    target_id: UUID


TEST_DATA = [
    # Search for TV
    TestData(
        query="The Bear",
        name="the-bear",
        target_id=UUID("05eb6a8e-90ed-4947-8c0b-e6536cbddd5f"),
    ),
    # Search for movie
    TestData(
        query="The Wolf of Wall Street",
        name="the-wolf-of-wall-street",
        target_id=UUID("4ee4f57e-19bd-493f-96f9-ad3e753af981"),
    ),
]


@pytest.fixture(scope="session")
def endpoint(client: Wholoo) -> Search:
    return client.search


@pytest.fixture(params=TEST_DATA, ids=lambda test_data: test_data.name)
def test_data(request: pytest.FixtureRequest) -> TestData:
    return request.param


class TestSearch:
    def test_download(self, endpoint: Search, test_data: TestData) -> None:
        download_and_save(
            endpoint,
            test_data.name,
            lambda: endpoint.download(test_data.query, limit=1),
        )

    def test_parse(self, endpoint: Search, test_data: TestData) -> None:
        search: SearchModel = parse_json(endpoint, test_data.name)
        top = search.groups[0].results[0].metrics_info
        assert top.target_id == test_data.target_id
        assert top.target_name == test_data.query
