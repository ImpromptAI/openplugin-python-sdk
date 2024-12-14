# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    info,
    processors,
    plugin_validators,
    function_providers,
    openapi_param_parsers,
    run_function_providers,
    function_provider_requests,
    plugin_execution_pipelines,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, OpenpluginError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Openplugin",
    "AsyncOpenplugin",
    "Client",
    "AsyncClient",
]


class Openplugin(SyncAPIClient):
    info: info.InfoResource
    plugin_execution_pipelines: plugin_execution_pipelines.PluginExecutionPipelinesResource
    processors: processors.ProcessorsResource
    function_providers: function_providers.FunctionProvidersResource
    function_provider_requests: function_provider_requests.FunctionProviderRequestsResource
    run_function_providers: run_function_providers.RunFunctionProvidersResource
    plugin_validators: plugin_validators.PluginValidatorsResource
    openapi_param_parsers: openapi_param_parsers.OpenAPIParamParsersResource
    with_raw_response: OpenpluginWithRawResponse
    with_streaming_response: OpenpluginWithStreamedResponse

    # client options
    x_api_key: str

    def __init__(
        self,
        *,
        x_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous openplugin client instance.

        This automatically infers the `x_api_key` argument from the `OPENPLUGIN_API_KEY` environment variable if it is not provided.
        """
        if x_api_key is None:
            x_api_key = os.environ.get("OPENPLUGIN_API_KEY")
        if x_api_key is None:
            raise OpenpluginError(
                "The x_api_key client option must be set either by passing x_api_key to the client or by setting the OPENPLUGIN_API_KEY environment variable"
            )
        self.x_api_key = x_api_key

        if base_url is None:
            base_url = os.environ.get("OPENPLUGIN_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:8003"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.info = info.InfoResource(self)
        self.plugin_execution_pipelines = plugin_execution_pipelines.PluginExecutionPipelinesResource(self)
        self.processors = processors.ProcessorsResource(self)
        self.function_providers = function_providers.FunctionProvidersResource(self)
        self.function_provider_requests = function_provider_requests.FunctionProviderRequestsResource(self)
        self.run_function_providers = run_function_providers.RunFunctionProvidersResource(self)
        self.plugin_validators = plugin_validators.PluginValidatorsResource(self)
        self.openapi_param_parsers = openapi_param_parsers.OpenAPIParamParsersResource(self)
        self.with_raw_response = OpenpluginWithRawResponse(self)
        self.with_streaming_response = OpenpluginWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        x_api_key = self.x_api_key
        return {"x-api-key": x_api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        x_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            x_api_key=x_api_key or self.x_api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncOpenplugin(AsyncAPIClient):
    info: info.AsyncInfoResource
    plugin_execution_pipelines: plugin_execution_pipelines.AsyncPluginExecutionPipelinesResource
    processors: processors.AsyncProcessorsResource
    function_providers: function_providers.AsyncFunctionProvidersResource
    function_provider_requests: function_provider_requests.AsyncFunctionProviderRequestsResource
    run_function_providers: run_function_providers.AsyncRunFunctionProvidersResource
    plugin_validators: plugin_validators.AsyncPluginValidatorsResource
    openapi_param_parsers: openapi_param_parsers.AsyncOpenAPIParamParsersResource
    with_raw_response: AsyncOpenpluginWithRawResponse
    with_streaming_response: AsyncOpenpluginWithStreamedResponse

    # client options
    x_api_key: str

    def __init__(
        self,
        *,
        x_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async openplugin client instance.

        This automatically infers the `x_api_key` argument from the `OPENPLUGIN_API_KEY` environment variable if it is not provided.
        """
        if x_api_key is None:
            x_api_key = os.environ.get("OPENPLUGIN_API_KEY")
        if x_api_key is None:
            raise OpenpluginError(
                "The x_api_key client option must be set either by passing x_api_key to the client or by setting the OPENPLUGIN_API_KEY environment variable"
            )
        self.x_api_key = x_api_key

        if base_url is None:
            base_url = os.environ.get("OPENPLUGIN_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:8003"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.info = info.AsyncInfoResource(self)
        self.plugin_execution_pipelines = plugin_execution_pipelines.AsyncPluginExecutionPipelinesResource(self)
        self.processors = processors.AsyncProcessorsResource(self)
        self.function_providers = function_providers.AsyncFunctionProvidersResource(self)
        self.function_provider_requests = function_provider_requests.AsyncFunctionProviderRequestsResource(self)
        self.run_function_providers = run_function_providers.AsyncRunFunctionProvidersResource(self)
        self.plugin_validators = plugin_validators.AsyncPluginValidatorsResource(self)
        self.openapi_param_parsers = openapi_param_parsers.AsyncOpenAPIParamParsersResource(self)
        self.with_raw_response = AsyncOpenpluginWithRawResponse(self)
        self.with_streaming_response = AsyncOpenpluginWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        x_api_key = self.x_api_key
        return {"x-api-key": x_api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        x_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            x_api_key=x_api_key or self.x_api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class OpenpluginWithRawResponse:
    def __init__(self, client: Openplugin) -> None:
        self.info = info.InfoResourceWithRawResponse(client.info)
        self.plugin_execution_pipelines = plugin_execution_pipelines.PluginExecutionPipelinesResourceWithRawResponse(
            client.plugin_execution_pipelines
        )
        self.processors = processors.ProcessorsResourceWithRawResponse(client.processors)
        self.function_providers = function_providers.FunctionProvidersResourceWithRawResponse(client.function_providers)
        self.function_provider_requests = function_provider_requests.FunctionProviderRequestsResourceWithRawResponse(
            client.function_provider_requests
        )
        self.run_function_providers = run_function_providers.RunFunctionProvidersResourceWithRawResponse(
            client.run_function_providers
        )
        self.plugin_validators = plugin_validators.PluginValidatorsResourceWithRawResponse(client.plugin_validators)
        self.openapi_param_parsers = openapi_param_parsers.OpenAPIParamParsersResourceWithRawResponse(
            client.openapi_param_parsers
        )


class AsyncOpenpluginWithRawResponse:
    def __init__(self, client: AsyncOpenplugin) -> None:
        self.info = info.AsyncInfoResourceWithRawResponse(client.info)
        self.plugin_execution_pipelines = (
            plugin_execution_pipelines.AsyncPluginExecutionPipelinesResourceWithRawResponse(
                client.plugin_execution_pipelines
            )
        )
        self.processors = processors.AsyncProcessorsResourceWithRawResponse(client.processors)
        self.function_providers = function_providers.AsyncFunctionProvidersResourceWithRawResponse(
            client.function_providers
        )
        self.function_provider_requests = (
            function_provider_requests.AsyncFunctionProviderRequestsResourceWithRawResponse(
                client.function_provider_requests
            )
        )
        self.run_function_providers = run_function_providers.AsyncRunFunctionProvidersResourceWithRawResponse(
            client.run_function_providers
        )
        self.plugin_validators = plugin_validators.AsyncPluginValidatorsResourceWithRawResponse(
            client.plugin_validators
        )
        self.openapi_param_parsers = openapi_param_parsers.AsyncOpenAPIParamParsersResourceWithRawResponse(
            client.openapi_param_parsers
        )


class OpenpluginWithStreamedResponse:
    def __init__(self, client: Openplugin) -> None:
        self.info = info.InfoResourceWithStreamingResponse(client.info)
        self.plugin_execution_pipelines = (
            plugin_execution_pipelines.PluginExecutionPipelinesResourceWithStreamingResponse(
                client.plugin_execution_pipelines
            )
        )
        self.processors = processors.ProcessorsResourceWithStreamingResponse(client.processors)
        self.function_providers = function_providers.FunctionProvidersResourceWithStreamingResponse(
            client.function_providers
        )
        self.function_provider_requests = (
            function_provider_requests.FunctionProviderRequestsResourceWithStreamingResponse(
                client.function_provider_requests
            )
        )
        self.run_function_providers = run_function_providers.RunFunctionProvidersResourceWithStreamingResponse(
            client.run_function_providers
        )
        self.plugin_validators = plugin_validators.PluginValidatorsResourceWithStreamingResponse(
            client.plugin_validators
        )
        self.openapi_param_parsers = openapi_param_parsers.OpenAPIParamParsersResourceWithStreamingResponse(
            client.openapi_param_parsers
        )


class AsyncOpenpluginWithStreamedResponse:
    def __init__(self, client: AsyncOpenplugin) -> None:
        self.info = info.AsyncInfoResourceWithStreamingResponse(client.info)
        self.plugin_execution_pipelines = (
            plugin_execution_pipelines.AsyncPluginExecutionPipelinesResourceWithStreamingResponse(
                client.plugin_execution_pipelines
            )
        )
        self.processors = processors.AsyncProcessorsResourceWithStreamingResponse(client.processors)
        self.function_providers = function_providers.AsyncFunctionProvidersResourceWithStreamingResponse(
            client.function_providers
        )
        self.function_provider_requests = (
            function_provider_requests.AsyncFunctionProviderRequestsResourceWithStreamingResponse(
                client.function_provider_requests
            )
        )
        self.run_function_providers = run_function_providers.AsyncRunFunctionProvidersResourceWithStreamingResponse(
            client.run_function_providers
        )
        self.plugin_validators = plugin_validators.AsyncPluginValidatorsResourceWithStreamingResponse(
            client.plugin_validators
        )
        self.openapi_param_parsers = openapi_param_parsers.AsyncOpenAPIParamParsersResourceWithStreamingResponse(
            client.openapi_param_parsers
        )


Client = Openplugin

AsyncClient = AsyncOpenplugin
