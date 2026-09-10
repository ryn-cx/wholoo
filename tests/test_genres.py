from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wholoo import Wholoo


def test_download(client: Wholoo) -> None:
    genres = client.genres()
    assert genres.items
    assert all(genre.href.startswith("/hub/") for genre in genres.items)
