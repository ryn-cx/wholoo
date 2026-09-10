# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from wholoo.exceptions import HTTPError, SeriesNotFoundError

if TYPE_CHECKING:
    from wholoo import Wholoo

SERIES_IDS = [
    pytest.param("fdeb1018-4472-442f-ba94-fb087cdea069", id="bob's burgers"),
]


# TODO: Validate
@pytest.mark.parametrize("content_id", SERIES_IDS)
def test_download(client: Wholoo, content_id: str) -> None:
    series = client.tv(content_id)
    assert str(series.id) == content_id
    assert series.components


# TODO: Validate
def test_download_invalid(client: Wholoo) -> None:
    with pytest.raises(SeriesNotFoundError):
        client.tv.download("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")


# TODO: Validate
def test_download_malformed(client: Wholoo) -> None:
    with pytest.raises(HTTPError):
        client.tv.download("AAAAAAAA")
