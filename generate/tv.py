# TODO: Validate
"""Rebuilds TVModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, WHOLOO_PATH
from generate.utils import download_if_missing
from wholoo import Wholoo

CONTENT_IDS = ["fdeb1018-4472-442f-ba94-fb087cdea069"]


# TODO: Validate
def generate_tv(client: Wholoo) -> None:
    """Rebuild TVModel."""
    for content_id in CONTENT_IDS:
        download_if_missing(
            FILES_PATH,
            "TVModel",
            content_id,
            lambda content_id=content_id: client.tv.download(content_id),
        )
    generate_model(FILES_PATH, WHOLOO_PATH, "TVModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_tv(Wholoo(build_client_automatically()))
