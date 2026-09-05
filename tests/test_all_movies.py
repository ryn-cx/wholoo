# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from tests.utils import RecordedEndpoint
from wholoo.all_movies.models import AllMoviesModel

if TYPE_CHECKING:
    from wholoo import Wholoo

NAME = "movies"
"""The movie list is one page, so its recording is filed under one name."""


# TODO: Validate
class AllMoviesTest(RecordedEndpoint):
    MODEL = AllMoviesModel
    # The build the page was served by is new on every deploy, and the movies
    # the site lists come and go from the service.
    IGNORED = ("AllMoviesModel.build_id", "Component.items")


# TODO: Validate
def test_download(client: Wholoo) -> None:
    AllMoviesTest.download_test(NAME, client.all_movies.download)


# TODO: Validate
def test_parse(client: Wholoo) -> None:
    all_movies = client.all_movies.load(AllMoviesTest.recorded_content(NAME))
    components = all_movies.props.page_props.layout.components
    listed = [
        item
        for component in components
        if component.type == "list_card"
        for item in component.items or []
    ]
    assert listed
    assert all(movie.href.startswith("/movie/") for movie in listed)
