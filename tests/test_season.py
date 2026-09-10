# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from wholoo.exceptions import SeasonNotFoundError

if TYPE_CHECKING:
    from wholoo import Wholoo

SEASONS = [
    pytest.param(
        "fdeb1018-4472-442f-ba94-fb087cdea069",
        2,
        id="bob's burgers season 2",
    ),
    # A season part way through airing lists episodes that cannot be played yet,
    # and those come without a runtime.
    pytest.param(
        "77db3944-8426-4259-94c8-be147d3e7594",
        3,
        id="smiling friends season 3",
    ),
]


# TODO: Validate
@pytest.mark.parametrize(("series_id", "season_number"), SEASONS)
def test_download(client: Wholoo, series_id: str, season_number: int) -> None:
    season = client.season(series_id, season_number)
    assert season.id == f"{series_id}::{season_number}"
    assert season.series_grouping_metadata.season_number == season_number
    assert season.items
    assert all(str(item.series_id) == series_id for item in season.items)


# TODO: Validate
def test_download_missing_season(client: Wholoo) -> None:
    season = client.season("fdeb1018-4472-442f-ba94-fb087cdea069", 999)
    assert not season.items


# TODO: Validate
def test_download_invalid(client: Wholoo) -> None:
    with pytest.raises(SeasonNotFoundError):
        client.season.download("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", 1)
