from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wholoo import Wholoo


def test_download(client: Wholoo) -> None:
    all_series = client.all_series()
    assert all_series.items
    assert all(series.href.startswith("/series/") for series in all_series.items)
