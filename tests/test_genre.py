from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from wholoo.exceptions import GenreNotFoundError

if TYPE_CHECKING:
    from wholoo import Wholoo

GENRE_IDS = ["action"]


@pytest.mark.parametrize("genre_id", GENRE_IDS)
def test_download(client: Wholoo, genre_id: str) -> None:
    genre = client.genre(genre_id)
    assert genre.items
    assert all(
        title.href.startswith(("/movie/", "/series/", "/watch/"))
        for title in genre.items
    )


def test_download_invalid(client: Wholoo) -> None:
    with pytest.raises(GenreNotFoundError):
        client.genre.download("qwert")
