# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from wholoo.exceptions import GenreNotFoundError
from wholoo.genre.models import GenreModel

if TYPE_CHECKING:
    from wholoo import Wholoo

GENRE_IDS = ["action", "anime-tv", "documentaries-movies"]

MISSING_GENRE_ID = "zzqqxxwwvvjjkk"


# TODO: Validate
class GenreTest(RecordedEndpoint):
    MODEL = GenreModel
    # The build the page was served by is new on every deploy, and the titles a
    # genre holds change as they come and go from the service.
    IGNORED = ("GenreModel.build_id", "Component.items")


# TODO: Validate
@pytest.mark.parametrize("genre_id", GENRE_IDS)
def test_download(client: Wholoo, genre_id: str) -> None:
    GenreTest.download_test(genre_id, lambda: client.genre.download(genre_id))


# TODO: Validate
@pytest.mark.parametrize("genre_id", GENRE_IDS)
def test_parse(client: Wholoo, genre_id: str) -> None:
    genre = client.genre.load(GenreTest.recorded_content(genre_id))
    components = genre.props.page_props.layout.components
    listed = [
        item
        for component in components
        if component.type == "list_card"
        for item in component.items or []
    ]
    assert listed
    assert all(
        title.href.startswith(("/movie/", "/series/", "/watch/")) for title in listed
    )


# TODO: Validate
def test_missing_genre(client: Wholoo) -> None:
    GenreTest.error_test(
        MISSING_GENRE_ID,
        lambda: client.genre.download(MISSING_GENRE_ID),
        GenreNotFoundError,
    )
