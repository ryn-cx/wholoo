# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from wholoo import Wholoo
    from wholoo.season import Season


class SeasonCase(BaseModel):
    """A season response to download, parse, and check."""

    series_id: UUID
    """The Hulu series id to download."""
    season: int
    """The season number to fetch."""
    name: str
    """A safe filename for the recorded response."""
    episode_count: int
    """The number of episodes the response should list."""


CASES = [
    SeasonCase(
        series_id=UUID("77db3944-8426-4259-94c8-be147d3e7594"),
        season=3,
        name="smiling-friends-season-3",
        episode_count=10,
    ),
]


@pytest.fixture(scope="session")
def endpoint(client: Wholoo) -> Season:
    return client.tv.season


@pytest.fixture(params=CASES, ids=lambda case: case.name)
def case(request: pytest.FixtureRequest) -> SeasonCase:
    return request.param


class TestSeason:
    def test_download(self, endpoint: Season, case: SeasonCase) -> None:
        download_and_save(
            endpoint,
            case.name,
            lambda: endpoint.download(str(case.series_id), case.season),
        )

    def test_parse(self, endpoint: Season, case: SeasonCase) -> None:
        season = parse_json(endpoint, case.name)
        assert season.series_grouping_metadata.season_number == case.season
        assert len(season.items) == case.episode_count
        assert all(item.season == str(case.season) for item in season.items)


def test_log_id(endpoint: Season) -> None:
    series_id = str(CASES[0].series_id)
    assert (
        endpoint.get_log_id(series_id, 3)
        == f"Season series_id={series_id!r} season=3"
    )
