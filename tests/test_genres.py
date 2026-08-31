# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from tests.utils import RecordedEndpoint
from wholoo.genres.models import GenresModel

if TYPE_CHECKING:
    from wholoo import Wholoo

NAME = "genres"
"""The genre list is one page, so its recording is filed under one name."""


# TODO: Validate
class GenresTest(RecordedEndpoint):
    MODEL = GenresModel
    # The build the page was served by is new on every deploy, and the genres
    # the site lists are added to and taken away from.
    IGNORED = ("GenresModel.build_id", "Component.items")


# TODO: Validate
def test_download(client: Wholoo) -> None:
    GenresTest.download_test(NAME, client.genres.download)


# TODO: Validate
def test_parse(client: Wholoo) -> None:
    genres = client.genres.load(GenresTest.recorded_content(NAME))
    components = genres.props.page_props.layout.components
    listed = [
        item
        for component in components
        if component.type == "list_card"
        for item in component.items or []
    ]
    assert listed
    assert "Action" in [genre.name for genre in listed]
    assert all(genre.href.startswith("/hub/") for genre in listed)
