# TODO: Validate
"""Contains the DiscoverHub class."""

from __future__ import annotations

import random
from logging import NullHandler, getLogger

from wholoo.base_api_endpoint import BaseEndpoint

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class DiscoverHub(BaseEndpoint):
    """Base class for the details hub of one title.

    A movie's details page and a series' details page are the same request with
    a different segment in the middle of the URL.

    - Example Request:
        - URL: https://www.hulu.com/{content_type}/{content_id}

        - Headers:
            - GET /content/v5/hubs/{content_type}/{content_id}?
                - schema=3&
                - limit=1999&
                - device_info=web:4.44.1&
                - referralHost=production&
                - cacheKey=0.31194440120842093&
                - pageType=DETAILS
                - HTTP/2
            - Host: discover.hulu.com
            - User-Agent: __REDACTED__
            - Accept: */*
            - Accept-Language: en-US,en;q=0.9
            - Accept-Encoding: gzip, deflate, br, zstd
            - Referer: https://www.hulu.com/{content_type}/{content_id}
            - Origin: https://www.hulu.com
            - Sec-Fetch-Dest: empty
            - Sec-Fetch-Mode: cors
            - Sec-Fetch-Site: same-site
            - Connection: keep-alive
            - Cookie: __REDACTED__
            - Priority: u=4
    """

    # TODO: Validate
    def _download(
        self,
        content_type: str,
        content_id: str,
        limit: int,
        log_id: str,
    ) -> str:
        """Download one title's details hub."""
        return self._client.download(
            endpoint=f"content/v5/hubs/{content_type}/{content_id}",
            params={
                "schema": "3",
                "limit": str(limit),
                "device_info": "web:4.44.1",
                "referralHost": "production",
                # A cache buster rather than anything the API reads.
                "cacheKey": str(random.random()),  # noqa: S311
                "pageType": "DETAILS",
            },
            headers={
                "Referer": f"https://www.hulu.com/{content_type}/{content_id}",
            },
            log_id=log_id,
        )
