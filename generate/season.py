# TODO: Validate
"""Rebuilds SeasonModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, WHOLOO_PATH
from generate.utils import download_if_missing
from wholoo import Wholoo

SEASONS = [
    ("fdeb1018-4472-442f-ba94-fb087cdea069", 2, "bobs-burgers-season-2"),
    ("77db3944-8426-4259-94c8-be147d3e7594", 3, "smiling-friends-season-3"),
]
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
    generate_model(FILES_PATH, WHOLOO_PATH, "SeasonModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_season(Wholoo(build_client_automatically()))
