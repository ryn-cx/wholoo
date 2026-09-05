# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

from tests.utils import RecordedEndpoint
from wholoo.all_series.models import AllSeriesModel

if TYPE_CHECKING:
    from wholoo import Wholoo

NAME = "series"
"""The series list is one page, so its recording is filed under one name."""


# TODO: Validate
class AllSeriesTest(RecordedEndpoint):
    MODEL = AllSeriesModel
    # The build the page was served by is new on every deploy, and the series
    # the site lists come and go from the service.
    IGNORED = ("AllSeriesModel.build_id", "Component.items")


# TODO: Validate
def test_download(client: Wholoo) -> None:
    AllSeriesTest.download_test(NAME, client.all_series.download)


# TODO: Validate
def test_parse(client: Wholoo) -> None:
    all_series = client.all_series.load(AllSeriesTest.recorded_content(NAME))
    components = all_series.props.page_props.layout.components
    listed = [
        item
        for component in components
        if component.type == "list_card"
        for item in component.items or []
    ]
    assert listed
    assert all(series.href.startswith("/series/") for series in listed)
