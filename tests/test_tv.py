from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest

from tests.utils import assert_error, download_and_save, parse_json
from wholoo.exceptions import HTTPError

if TYPE_CHECKING:
    from wholoo import Wholoo
    from wholoo.tv import TV


TEST_DATA = (UUID("fdeb1018-4472-442f-ba94-fb087cdea069"),)
INVALID_SERIES_ID_TEST_DATA = (UUID("AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA"), "AAAAAAAA")


@pytest.fixture(scope="session")
def endpoint(client: Wholoo) -> TV:
    return client.tv


@pytest.fixture(params=TEST_DATA, ids=str)
def test_data(request: pytest.FixtureRequest) -> UUID:
    return request.param


@pytest.fixture(params=INVALID_SERIES_ID_TEST_DATA, ids=str)
def invalid_series_id_test_data(request: pytest.FixtureRequest) -> UUID | str:
    return request.param


class TestTV:
    def test_download(self, endpoint: TV, test_data: UUID) -> None:
        download_and_save(
            endpoint,
            str(test_data),
            lambda: endpoint.download(str(test_data)),
        )

    def test_parse(self, endpoint: TV, test_data: UUID) -> None:
        series = parse_json(endpoint, str(test_data))
        assert series.id == test_data

    def test_invalid_content_id(
        self,
        endpoint: TV,
        invalid_series_id_test_data: UUID | str,
    ) -> None:
        test_data = invalid_series_id_test_data
        assert_error(
            endpoint,
            str(test_data),
            lambda: endpoint.download(str(test_data)),
            HTTPError,
        )
