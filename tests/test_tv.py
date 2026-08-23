# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from wholoo.exceptions import HTTPError, SeriesNotFoundError
from wholoo.tv.models import TVModel

if TYPE_CHECKING:
    from wholoo import Wholoo

CONTENT_IDS = [
    # https://www.hulu.com/series/fdeb1018-4472-442f-ba94-fb087cdea069
    pytest.param("fdeb1018-4472-442f-ba94-fb087cdea069", id="bob's burgers"),
]


# TODO: Validate
class TVTest(RecordedEndpoint):
    MODEL = TVModel


# TODO: Validate
@pytest.mark.parametrize("content_id", CONTENT_IDS)
def test_download(client: Wholoo, content_id: str) -> None:
    TVTest.download_test(content_id, lambda: client.tv.download(content_id))


# TODO: Validate
@pytest.mark.parametrize("content_id", CONTENT_IDS)
def test_parse(client: Wholoo, content_id: str) -> None:
    data = client.tv.load(TVTest.recorded_content(content_id))
    assert str(data.id) == content_id
    assert data.components


# TODO: Validate
@pytest.mark.parametrize(
    "content_id",
    [
        pytest.param(
            "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
            id="series that does not exist",
        ),
    ],
)
def test_download_invalid(client: Wholoo, content_id: str) -> None:
    TVTest.error_test(
        content_id,
        lambda: client.tv.download(content_id),
        SeriesNotFoundError,
    )


# TODO: Validate
@pytest.mark.parametrize(
    "content_id",
    [pytest.param("AAAAAAAA", id="id that is not shaped like one")],
)
def test_download_malformed(client: Wholoo, content_id: str) -> None:
    TVTest.error_test(
        content_id,
        lambda: client.tv.download(content_id),
        HTTPError,
    )
