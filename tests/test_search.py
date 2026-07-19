# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from wholoo import Wholoo
    from wholoo.search import Search


class SearchCase(BaseModel):
    """A search response to download, parse, and check."""

    query: str
    """The search text to download."""
    name: str
    """A safe filename for the recorded response of ``query``."""
    target_id: UUID
    """The id of the title expected as the top result for ``query``."""
    target_name: str
    """The name of the title expected as the top result for ``query``."""


CASES = [
    SearchCase(
        query="bob's burgers",
        name="bobs-burgers",
        target_id=UUID("fdeb1018-4472-442f-ba94-fb087cdea069"),
        target_name="Bob's Burgers",
    ),
    SearchCase(
        query="smiling friends",
        name="smiling-friends",
        target_id=UUID("77db3944-8426-4259-94c8-be147d3e7594"),
        target_name="Smiling Friends",
    ),
]


@pytest.fixture(scope="session")
def endpoint(client: Wholoo) -> Search:
    return client.search


@pytest.fixture(params=CASES, ids=lambda case: case.name)
def case(request: pytest.FixtureRequest) -> SearchCase:
    return request.param


class TestSearch:
    def test_download(self, endpoint: Search, case: SearchCase) -> None:
        download_and_save(
            endpoint,
            case.name,
            lambda: endpoint.download(case.query),
        )

    def test_parse(self, endpoint: Search, case: SearchCase) -> None:
        search = parse_json(endpoint, case.name)
        top = search.groups[0].results[0].metrics_info
        assert top.target_id == case.target_id
        assert top.target_name == case.target_name


def test_log_id(endpoint: Search) -> None:
    query = CASES[0].query
    assert endpoint.get_log_id(query) == f"Search query={query!r}"
