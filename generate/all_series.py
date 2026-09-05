# TODO: Validate
"""Rebuilds AllSeriesModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, WHOLOO_PATH
from generate.utils import download_if_missing, rebuild_model
from wholoo import Wholoo

NAME = "series"
"""The series list is one page, so its recording is filed under one name."""


# TODO: Validate
def generate_all_series(client: Wholoo) -> None:
    """Rebuild AllSeriesModel."""
    download_if_missing(FILES_PATH, "AllSeriesModel", NAME, client.all_series.download)
    rebuild_model(FILES_PATH, WHOLOO_PATH, "AllSeriesModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_all_series(Wholoo(build_client_automatically()))
