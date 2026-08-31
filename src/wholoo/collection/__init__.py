# TODO: Validate
"""Contains the Collection class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any

from wholoo.base_api_endpoint import BaseEndpoint
from wholoo.collection.models import CollectionModel, model_validate_json
from wholoo.exceptions import CollectionNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())

LIMIT = 15
"""How many titles a page holds, which is what the site asks for."""


# TODO: Validate
def page_all_etags(page: dict[str, Any]) -> set[str]:
    """Return the all_etag of every title on one page."""
    return {
        etag
        for item in page.get("items", [])
        if (etag := _playback_bundle(item).get("all_etag")) is not None
    }


# TODO: Validate
def _playback_bundle(item: dict[str, Any]) -> dict[str, Any]:
    """Return the playback bundle of one title, which is where its etags are."""
    playback = item.get("actions", {}).get("playback") or {}
    return playback.get("bundle") or {}


# TODO: Validate
class Collection(BaseEndpoint):
    """Manage one hub collection's file.

    A collection is a row of titles on a hub page, served a page at a time
    newest first.

    Source: https://www.hulu.com/hub/{hub}

    Example request:
        - GET /content/v5/view_hubs/{hub}/collections/{collection_id}?
            - limit=15&
            - schema=3&
            - limit=15&
            - offset=0
            - HTTP/2
        - Host: discover.hulu.com
        - User-Agent: __REDACTED__
        - Accept: */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://www.hulu.com/hub/{hub}
        - Origin: https://www.hulu.com
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-site
        - Connection: keep-alive
        - Cookie: __REDACTED__
        - Priority: u=4
    """

    # TODO: Validate
    def __call__(
        self,
        hub: str,
        collection_id: str,
        all_etags: list[str],
        *,
        limit: int = LIMIT,
    ) -> list[CollectionModel]:
        """Walk the collection and return the model each page is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        pages = self.download_until_all_etag_is_found(
            hub,
            collection_id,
            all_etags,
            limit=limit,
        )
        return [self.load(page, log_id) for page in pages]

    # TODO: Validate
    def download_until_all_etag_is_found(
        self,
        hub: str,
        collection_id: str,
        all_etags: list[str],
        *,
        limit: int = LIMIT,
    ) -> list[str]:
        """Download the collection a page at a time, until it runs out.

        Stops on the page carrying any of `all_etags`, so a collection walked to
        pick up what was added since last time only reaches back as far as a
        title it already has. An empty list runs to the end of the collection.
        """
        wanted_etags = set(all_etags)
        pages: list[str] = []
        offset = 0
        while True:
            page = self.download(hub, collection_id, offset=offset, limit=limit)
            pages.append(page)
            parsed = json.loads(page)
            if page_all_etags(parsed) & wanted_etags:
                return pages
            if not parsed["pagination"].get("next"):
                return pages
            offset += limit

    # TODO: Validate
    def download(
        self,
        hub: str,
        collection_id: str,
        *,
        offset: int = 0,
        limit: int = LIMIT,
    ) -> str:
        """Download one page of the collection."""
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download(
                endpoint=f"content/v5/view_hubs/{hub}/collections/{collection_id}",
                params=[
                    ("limit", str(limit)),
                    ("schema", "3"),
                    # The site sends limit twice, and so does this.
                    ("limit", str(limit)),
                    ("offset", str(offset)),
                ],
                headers={"Referer": f"https://www.hulu.com/hub/{hub}"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise CollectionNotFoundError(
                hub,
                collection_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> CollectionModel:
        """Read one downloaded page of a collection into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
