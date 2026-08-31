# TODO: Validate
"""Rebuilds CollectionModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, WHOLOO_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from wholoo import Wholoo

PAGES = load_ids("CollectionModel")
"""The hub, collection and offset each recording is of, and its name."""


# TODO: Validate
def generate_collection(client: Wholoo) -> None:
    """Rebuild CollectionModel."""
    for hub, collection_id, offset, name in PAGES:
        download_if_missing(
            FILES_PATH,
            "CollectionModel",
            name,
            lambda hub=hub, collection_id=collection_id, offset=offset: (
                client.collection.download(hub, collection_id, offset=offset)
            ),
        )
    rebuild_model(
        FILES_PATH,
        WHOLOO_PATH,
        "CollectionModel",
        name_of=lambda page: page[3],
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_collection(Wholoo(build_client_automatically()))
