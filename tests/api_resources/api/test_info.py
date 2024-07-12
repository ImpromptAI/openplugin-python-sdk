# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openplugin import Openplugin, AsyncOpenplugin
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInfo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Openplugin) -> None:
        info = client.api.info.retrieve()
        assert_matches_type(object, info, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Openplugin) -> None:
        response = client.api.info.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        info = response.parse()
        assert_matches_type(object, info, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Openplugin) -> None:
        with client.api.info.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            info = response.parse()
            assert_matches_type(object, info, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInfo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenplugin) -> None:
        info = await async_client.api.info.retrieve()
        assert_matches_type(object, info, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenplugin) -> None:
        response = await async_client.api.info.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        info = await response.parse()
        assert_matches_type(object, info, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenplugin) -> None:
        async with async_client.api.info.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            info = await response.parse()
            assert_matches_type(object, info, path=["response"])

        assert cast(Any, response.is_closed) is True
