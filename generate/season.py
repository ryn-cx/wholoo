# TODO: Validate
"""Rebuilds SeasonModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, WHOLOO_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from wholoo import Wholoo

SEASONS = load_ids("SeasonModel")
"""The series and season each recording is of, and the name it is filed under."""


# TODO: Validate
def generate_season(client: Wholoo) -> None:
    """Rebuild SeasonModel."""
    for series_id, season, name in SEASONS:
        download_if_missing(
            FILES_PATH,
            "SeasonModel",
            name,
            lambda series_id=series_id, season=season: client.season.download(
                series_id,
                season,
            ),
        )
    rebuild_model(
        FILES_PATH,
        WHOLOO_PATH,
        "SeasonModel",
        name_of=lambda season: season[2],
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_season(Wholoo(build_client_automatically()))
