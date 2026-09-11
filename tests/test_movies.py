# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from wholoo.exceptions import HTTPError, MovieNotFoundError

if TYPE_CHECKING:
    from wholoo import Wholoo

MOVIE_IDS = [
    pytest.param("4ee4f57e-19bd-493f-96f9-ad3e753af981", id="Movie"),
]


# TODO: Validate
@pytest.mark.parametrize("content_id", MOVIE_IDS)
def test_download(client: Wholoo, content_id: str) -> None:
    movie = client.movies(content_id)
    assert str(movie.details.entity.id) == content_id
    assert movie.details.entity.name


# TODO: Validate
def test_download_invalid(client: Wholoo) -> None:
    with pytest.raises(MovieNotFoundError):
        client.movies.download("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")


# TODO: Validate
def test_download_malformed(client: Wholoo) -> None:
    with pytest.raises(HTTPError):
        client.movies.download("AAAAAAAA")
