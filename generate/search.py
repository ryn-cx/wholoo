# TODO: Validate
"""Rebuilds SearchModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, WHOLOO_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from wholoo import Wholoo

LIMIT = 1
"""The recordings were made asking for one result."""

QUERIES = load_ids("SearchModel")
"""Each query and the name its recording is filed under."""


# TODO: Validate
def generate_search(client: Wholoo) -> None:
    """Rebuild SearchModel."""
    for query, name in QUERIES:
        download_if_missing(
            FILES_PATH,
            "SearchModel",
            name,
            lambda query=query: client.search.download(query, limit=LIMIT),
        )
    rebuild_model(
        FILES_PATH,
        WHOLOO_PATH,
        "SearchModel",
        name_of=lambda query: query[1],
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search(Wholoo(build_client_automatically()))
