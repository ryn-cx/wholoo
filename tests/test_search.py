# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from wholoo import Wholoo

QUERIES = [
    pytest.param("The Bear", "series", id="series"),
    pytest.param("The Wolf of Wall Street", "movie", id="movie"),
]


# TODO: Validate
@pytest.mark.parametrize(("query", "target_type"), QUERIES)
def test_download(client: Wholoo, query: str, target_type: str) -> None:
    search = client.search(query)
    assert search.results
    assert query in [result.metrics_info.target_name for result in search.results]
    assert target_type in [result.metrics_info.target_type for result in search.results]


# TODO: Validate
def test_download_invalid(client: Wholoo) -> None:
    # A query matching no title is still answered with whatever is nearest.
    search = client.search("zzqqxxwwvvjjkk")
    assert search.results
