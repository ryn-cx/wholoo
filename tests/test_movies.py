from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest

from tests.utils import assert_error, download_and_save, parse_json
from wholoo.exceptions import HTTPError

if TYPE_CHECKING:
    from wholoo import Wholoo
    from wholoo.movies import Movies


TEST_DATA = (UUID("4ee4f57e-19bd-493f-96f9-ad3e753af981"),)
INVALID_MOVIE_ID_TEST_DATA = (UUID("AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA"), "AAAAAAAA")


@pytest.fixture(scope="session")
def endpoint(client: Wholoo) -> Movies:
    return client.movies


@pytest.fixture(params=TEST_DATA, ids=str)
def test_data(request: pytest.FixtureRequest) -> UUID:
    return request.param


@pytest.fixture(params=INVALID_MOVIE_ID_TEST_DATA, ids=str)
def invalid_movie_id_test_data(request: pytest.FixtureRequest) -> UUID | str:
    return request.param


class TestMovies:
    def test_download(self, endpoint: Movies, test_data: UUID) -> None:
        download_and_save(
            endpoint,
            str(test_data),
            lambda: endpoint.download(str(test_data)),
        )

    def test_parse(self, endpoint: Movies, test_data: UUID) -> None:
        movie = parse_json(endpoint, str(test_data))
        assert movie.id == test_data

    def test_invalid_content_id(
        self,
        endpoint: Movies,
        invalid_movie_id_test_data: UUID | str,
    ) -> None:
        test_data = invalid_movie_id_test_data
        assert_error(
            endpoint,
            str(test_data),
            lambda: endpoint.download(str(test_data)),
            HTTPError,
        )
