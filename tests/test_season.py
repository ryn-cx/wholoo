# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from wholoo.exceptions import SeasonNotFoundError
from wholoo.season.models import SeasonModel

if TYPE_CHECKING:
    from wholoo import Wholoo

SEASONS = [
    # https://www.hulu.com/series/fdeb1018-4472-442f-ba94-fb087cdea069
    pytest.param(
        "fdeb1018-4472-442f-ba94-fb087cdea069",
        2,
        "bobs-burgers-season-2",
        id="bob's burgers season 2",
    ),
    # A season part way through airing lists episodes that cannot be played
    # yet, and those come without a runtime.
    # https://www.hulu.com/series/77db3944-8426-4259-94c8-be147d3e7594
    pytest.param(
        "77db3944-8426-4259-94c8-be147d3e7594",
        3,
        "smiling-friends-season-3",
        id="smiling friends season 3",
    ),
]


# TODO: Validate
class SeasonTest(RecordedEndpoint):
    MODEL = SeasonModel


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season", "name"), SEASONS)
def test_download(client: Wholoo, series_id: str, season: int, name: str) -> None:
    SeasonTest.download_test(name, lambda: client.season.download(series_id, season))


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season", "name"), SEASONS)
def test_parse(client: Wholoo, series_id: str, season: int, name: str) -> None:
    data = client.season.load(SeasonTest.recorded_content(name))
    assert data.id == f"{series_id}::{season}"
    assert data.series_grouping_metadata.season_number == season
    assert data.items
    assert all(str(item.series_id) == series_id for item in data.items)


# TODO: Validate
@pytest.mark.parametrize(
    ("series_id", "season", "name"),
    [
        pytest.param(
            "fdeb1018-4472-442f-ba94-fb087cdea069",
            999,
            "bobs-burgers-season-999",
            id="season the series does not have",
        ),
        pytest.param(
            "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
            1,
            "unknown-series-season-1",
            id="series that does not exist",
        ),
    ],
)
def test_download_invalid(
    client: Wholoo,
    series_id: str,
    season: int,
    name: str,
) -> None:
    SeasonTest.error_test(
        name,
        lambda: client.season.download(series_id, season),
        SeasonNotFoundError,
    )
