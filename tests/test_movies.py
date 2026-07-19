# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from wholoo import Wholoo
    from wholoo.movies import Movies


class MoviesCase(BaseModel):
    """A movies response to download, parse, and check."""

    movie_id: UUID
    """The Hulu movie id to download and the id every response should report."""
    name: str
    """A safe filename for the recorded response of ``movie_id``."""
    title: str
    """The movie name every response for ``movie_id`` should report."""


CASES = [
    MoviesCase(
        movie_id=UUID("4ee4f57e-19bd-493f-96f9-ad3e753af981"),
        name="the-wolf-of-wall-street",
        title="The Wolf of Wall Street",
    ),
]


@pytest.fixture(scope="session")
def endpoint(client: Wholoo) -> Movies:
    return client.movies


@pytest.fixture(params=CASES, ids=lambda case: case.name)
def case(request: pytest.FixtureRequest) -> MoviesCase:
    return request.param


class TestMovies:
    def test_download(self, endpoint: Movies, case: MoviesCase) -> None:
        download_and_save(
            endpoint,
            case.name,
            lambda: endpoint.download(str(case.movie_id)),
        )

    def test_parse(self, endpoint: Movies, case: MoviesCase) -> None:
        movie = parse_json(endpoint, case.name)
        assert movie.id == case.movie_id
        assert movie.name == case.title


def test_log_id(endpoint: Movies) -> None:
    movie_id = str(CASES[0].movie_id)
    assert endpoint.get_log_id(movie_id) == f"Movies content_id={movie_id!r}"
