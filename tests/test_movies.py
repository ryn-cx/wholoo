# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from wholoo.exceptions import HTTPError, MovieNotFoundError
from wholoo.movies.models import MoviesModel

if TYPE_CHECKING:
    from wholoo import Wholoo

CONTENT_IDS = [
    # https://www.hulu.com/movie/4ee4f57e-19bd-493f-96f9-ad3e753af981
    pytest.param("4ee4f57e-19bd-493f-96f9-ad3e753af981", id="the wolf of wall street"),
]


# TODO: Validate
class MoviesTest(RecordedEndpoint):
    MODEL = MoviesModel


# TODO: Validate
@pytest.mark.parametrize("content_id", CONTENT_IDS)
def test_download(client: Wholoo, content_id: str) -> None:
    MoviesTest.download_test(content_id, lambda: client.movies.download(content_id))


# TODO: Validate
@pytest.mark.parametrize("content_id", CONTENT_IDS)
def test_parse(client: Wholoo, content_id: str) -> None:
    data = client.movies.load(MoviesTest.recorded_content(content_id))
    assert str(data.id) == content_id
    assert data.details.entity


# TODO: Validate
@pytest.mark.parametrize(
    "content_id",
    [
        pytest.param(
            "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
            id="movie that does not exist",
        ),
    ],
)
def test_download_invalid(client: Wholoo, content_id: str) -> None:
    MoviesTest.error_test(
        content_id,
        lambda: client.movies.download(content_id),
        MovieNotFoundError,
    )


# TODO: Validate
@pytest.mark.parametrize(
    "content_id",
    [pytest.param("AAAAAAAA", id="id that is not shaped like one")],
)
def test_download_malformed(client: Wholoo, content_id: str) -> None:
    MoviesTest.error_test(
        content_id,
        lambda: client.movies.download(content_id),
        HTTPError,
    )
