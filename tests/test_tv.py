# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from wholoo import Wholoo
    from wholoo.tv import TV


class TVCase(BaseModel):
    """A series response to download, parse, and check."""

    series_id: UUID
    """The Hulu series id to download and the id every response should report."""
    name: str
    """A safe filename for the recorded response of ``series_id``."""
    title: str
    """The series name every response for ``series_id`` should report."""


CASES = [
    TVCase(
        series_id=UUID("fdeb1018-4472-442f-ba94-fb087cdea069"),
        name="bobs-burgers",
        title="Bob's Burgers",
    ),
]


@pytest.fixture(scope="session")
def endpoint(client: Wholoo) -> TV:
    return client.tv


@pytest.fixture(params=CASES, ids=lambda case: case.name)
def case(request: pytest.FixtureRequest) -> TVCase:
    return request.param


class TestTV:
    def test_download(self, endpoint: TV, case: TVCase) -> None:
        download_and_save(
            endpoint,
            case.name,
            lambda: endpoint.download(str(case.series_id)),
        )

    def test_parse(self, endpoint: TV, case: TVCase) -> None:
        series = parse_json(endpoint, case.name)
        assert series.id == case.series_id
        assert series.name == case.title


def test_log_id(endpoint: TV) -> None:
    series_id = str(CASES[0].series_id)
    assert endpoint.get_log_id(series_id) == f"TV content_id={series_id!r}"
