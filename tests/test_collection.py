# TODO: Validate
from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.utils import RecordedEndpoint
from wholoo.collection import page_all_etags
from wholoo.collection.models import CollectionModel
from wholoo.exceptions import CollectionNotFoundError, HTTPError

if TYPE_CHECKING:
    from wholoo import Wholoo

HUB = "movies"

COLLECTION_IDS = [
    # https://www.hulu.com/hub/movies
    pytest.param("11348", id="newly added movies"),
    pytest.param("2673", id="action movies"),
]

TOP_MOVIES_ID = "10022"
"""A collection short enough to walk to the end of in one page."""


# TODO: Validate
class CollectionTest(RecordedEndpoint):
    MODEL = CollectionModel
    # A collection is the titles the hub is showing right now, so which titles
    # are on a page is what it is expected to change. The strict model still
    # has to read every one of them, which is what the parse test holds it to.
    IGNORED = ("CollectionModel.items", "CollectionModel.p13n_href")


# TODO: Validate
@pytest.mark.parametrize("collection_id", COLLECTION_IDS)
def test_download(client: Wholoo, collection_id: str) -> None:
    CollectionTest.download_test(
        collection_id,
        lambda: client.collection.download(HUB, collection_id),
    )


# TODO: Validate
@pytest.mark.parametrize("collection_id", COLLECTION_IDS)
def test_parse(client: Wholoo, collection_id: str) -> None:
    collection = client.collection.load(
        CollectionTest.recorded_content(collection_id),
    )
    assert collection.id == collection_id
    assert collection.items


# TODO: Validate
def test_download_until_all_etag_is_found_reaches_the_end(client: Wholoo) -> None:
    pages = client.collection.download_until_all_etag_is_found(
        HUB,
        TOP_MOVIES_ID,
        [],
        limit=999,
    )
    assert len(pages) == 1
    assert client.collection.load(pages[0]).pagination.next is None


# TODO: Validate
def test_download_until_all_etag_is_found_pages_until_the_end(client: Wholoo) -> None:
    pages = client.collection.download_until_all_etag_is_found(
        HUB,
        TOP_MOVIES_ID,
        [],
        limit=5,
    )
    assert len(pages) > 1
    assert client.collection.load(pages[-1]).pagination.next is None


# TODO: Validate
def test_download_until_all_etag_is_found_stops_at_the_etag(client: Wholoo) -> None:
    first_page = client.collection.download(HUB, TOP_MOVIES_ID, limit=5)
    all_etag = next(iter(page_all_etags(json.loads(first_page))))

    pages = client.collection.download_until_all_etag_is_found(
        HUB,
        TOP_MOVIES_ID,
        [all_etag],
        limit=5,
    )

    assert len(pages) == 1
    assert all_etag in page_all_etags(json.loads(pages[0]))


# TODO: Validate
def test_download_until_all_etag_is_found_stops_at_any_of_the_etags(
    client: Wholoo,
) -> None:
    first_two_pages = client.collection.download_until_all_etag_is_found(
        HUB,
        TOP_MOVIES_ID,
        [],
        limit=5,
    )[:2]
    second_page_etag = next(iter(page_all_etags(json.loads(first_two_pages[1]))))

    pages = client.collection.download_until_all_etag_is_found(
        HUB,
        TOP_MOVIES_ID,
        ['"not an etag any title carries"', second_page_etag],
        limit=5,
    )

    assert len(pages) == len(first_two_pages)
    assert second_page_etag in page_all_etags(json.loads(pages[-1]))


# TODO: Validate
def test_download_until_all_etag_is_found_reaches_the_end_for_a_missing_etag(
    client: Wholoo,
) -> None:
    pages = client.collection.download_until_all_etag_is_found(
        HUB,
        TOP_MOVIES_ID,
        ['"not an etag any title carries"'],
        limit=5,
    )
    assert client.collection.load(pages[-1]).pagination.next is None


# TODO: Validate
@pytest.mark.parametrize(
    "collection_id",
    [pytest.param("99999999", id="collection that does not exist")],
)
def test_download_invalid(client: Wholoo, collection_id: str) -> None:
    CollectionTest.error_test(
        collection_id,
        lambda: client.collection.download(HUB, collection_id),
        CollectionNotFoundError,
    )


# TODO: Validate
@pytest.mark.parametrize(
    "collection_id",
    [pytest.param("AAAAAAAA", id="id that is not shaped like one")],
)
def test_download_malformed(client: Wholoo, collection_id: str) -> None:
    CollectionTest.error_test(
        collection_id,
        lambda: client.collection.download(HUB, collection_id),
        HTTPError,
    )
