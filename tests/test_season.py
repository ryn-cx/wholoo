from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest
from pydantic import BaseModel

from tests.utils import assert_error, download_and_save, parse_json
from wholoo.exceptions import HTTPError, InvalidSeasonError

if TYPE_CHECKING:
    from wholoo import Wholoo
    from wholoo.season import Season


class TestData(BaseModel):
    series_id: UUID | None
    season: int
    name: str


TEST_DATA = [
    TestData(
        series_id=UUID("77db3944-8426-4259-94c8-be147d3e7594"),
        season=3,
        name="smiling-friends-season-3",
    ),
]


INVALID_SERIES_ID_TEST_DATA = [
    TestData(
        series_id=UUID("AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA"),
        season=3,
        name="invalid-series-id",
    ),
]


INVALID_SEASON_TEST_DATA = [
    TestData(
        series_id=UUID("77db3944-8426-4259-94c8-be147d3e7594"),
        season=4,
        name="invalid-season",
    ),
]


@pytest.fixture(scope="session")
def endpoint(client: Wholoo) -> Season:
    return client.tv.season


@pytest.fixture(params=TEST_DATA, ids=lambda test_data: test_data.name)
def test_data(request: pytest.FixtureRequest) -> TestData:
    return request.param


@pytest.fixture(params=INVALID_SERIES_ID_TEST_DATA, ids=lambda test_data: test_data.name)
def invalid_series_id_test_data(request: pytest.FixtureRequest) -> TestData:
    return request.param


@pytest.fixture(params=INVALID_SEASON_TEST_DATA, ids=lambda test_data: test_data.name)
def invalid_season_test_data(request: pytest.FixtureRequest) -> TestData:
    return request.param


class TestSeason:
    def test_download(self, endpoint: Season, test_data: TestData) -> None:
        download_and_save(
            endpoint,
            test_data.name,
            lambda: endpoint.download(str(test_data.series_id), test_data.season),
        )

    def test_parse(self, endpoint: Season, test_data: TestData) -> None:
        season = parse_json(endpoint, test_data.name)
        assert season.id == f"{test_data.series_id}::{test_data.season}"

    def test_invalid_series_id(
        self,
        endpoint: Season,
        invalid_series_id_test_data: TestData,
    ) -> None:
        test_data = invalid_series_id_test_data
        assert_error(
            endpoint,
            test_data.name,
            lambda: endpoint.download(str(test_data.series_id), test_data.season),
            HTTPError,
        )

    def test_invalid_season(
        self,
        endpoint: Season,
        invalid_season_test_data: TestData,
    ) -> None:
        test_data = invalid_season_test_data
        assert_error(
            endpoint,
            test_data.name,
            lambda: endpoint.download(str(test_data.series_id), test_data.season),
            InvalidSeasonError,
        )