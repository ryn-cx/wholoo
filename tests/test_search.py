# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from wholoo.search.models import SearchModel

if TYPE_CHECKING:
    from wholoo import Wholoo

# The recordings were made asking for one result, so that is what the tests
# keep asking for.
LIMIT = 1

QUERIES = [
    pytest.param("The Bear", "the-bear", id="series"),
    pytest.param("The Wolf of Wall Street", "the-wolf-of-wall-street", id="movie"),
    # A query matching no title is still answered with whatever is nearest, so
    # what it lands on is not something to hold the test to.
    pytest.param("zzqqxxwwvvjjkk", "gibberish", id="gibberish"),
]

EXPECTED_TYPES = {"the-bear": "series", "the-wolf-of-wall-street": "movie"}
"""What kind of title each search is expected to match, where it is known."""


# TODO: Validate
class SearchTest(RecordedEndpoint):
    MODEL = SearchModel
    # A search is tagged with a tracking id that is new every time it is run.
    IGNORED = ("MetricsInfo.selection_tracking_id",)


# TODO: Validate
@pytest.mark.parametrize(("query", "name"), QUERIES)
def test_download(client: Wholoo, query: str, name: str) -> None:
    SearchTest.download_test(name, lambda: client.search.download(query, limit=LIMIT))


# TODO: Validate
@pytest.mark.parametrize(("query", "name"), QUERIES)
def test_parse(client: Wholoo, query: str, name: str) -> None:
    data = client.search.load(SearchTest.recorded_content(name))
    results = [result for group in data.groups for result in group.results]
    assert results

    expected_type = EXPECTED_TYPES.get(name)
    if expected_type is None:
        return
    assert query in [result.metrics_info.target_name for result in results]
    assert expected_type in [result.metrics_info.target_type for result in results]
