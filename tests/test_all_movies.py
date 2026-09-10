from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wholoo import Wholoo


def test_download(client: Wholoo) -> None:
    all_movies = client.all_movies()
    assert all_movies.items
    assert all(movie.href.startswith("/movie/") for movie in all_movies.items)
