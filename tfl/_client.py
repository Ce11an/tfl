"""Client to interact with the TFL API."""

import datetime
from collections.abc import Callable, Generator, Mapping
from typing import Any

import httpx
import pydantic
from httpx import AsyncBaseTransport

# noinspection PyProtectedMember
from httpx._config import DEFAULT_LIMITS, DEFAULT_MAX_REDIRECTS, DEFAULT_TIMEOUT_CONFIG, Limits

# noinspection PyProtectedMember
from httpx._types import (
    CertTypes,
    CookieTypes,
    HeaderTypes,
    ProxiesTypes,
    QueryParamTypes,
    TimeoutTypes,
    VerifyTypes,
)

from tfl import models

__all__ = ["Client", "Auth", "Response"]


class Response(pydantic.BaseModel):
    """Response model for Transport for London API.

    Args:
        received_time: The time the response was received.
        code: The HTTP status code.
        data: The data returned by the API.
    """

    received_time: datetime.datetime = pydantic.Field(
        title="Received Time",
        description="The time the response was received.",
        default_factory=datetime.datetime.now,
    )
    code: int = pydantic.Field(
        ...,
        title="Code",
        description="The HTTP status code.",
    )

    data: pydantic.BaseModel = pydantic.Field(
        ...,
        title="Data",
        description="The data returned by the API.",
    )


class Auth(httpx.Auth):
    """Auth class for Transport for London API.

    Args:
        key: The API key.
    """

    def __init__(self, key: str) -> None:
        self.key = key

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, Any, None]:
        """Add the API key to the request.

        Args:
            request: The request to be sent.

        Returns:
            The request with the API key added.
        """
        request.url = request.url.copy_add_param(key="app_key", value=self.key)
        yield request


# noinspection PyCompatibility
class Client(httpx.AsyncClient):
    """Client to interact with the TFL API.

    Args:
        auth: TFL authentication class to use when sending requests.
        params: Query parameters to include in request URLs, as a string, dictionary, or sequence of two-tuples.
        headers: Dictionary of HTTP headers to include when sending requests.
        cookies: Dictionary of Cookie items to include when sending requests.
        verify: SSL certificates (a.k.a CA bundle) used to verify the identity of requested hosts. Either `True`
            (default CA bundle), a path to an SSL certificate file, an `ssl.SSLContext`, or `False` (which will disable
             verification).
        cert: An SSL certificate used by the requested host to authenticate the client. Either a path to an SSL
            certificate file, or two-tuple of (certificate file, key file), or a three-tuple of (certificate file, key
            file, password).
        proxies: A dictionary mapping proxy keys to proxy URLs.
        timeout: The timeout configuration to use when sending requests.
        limits: The limits configuration to use.
        max_redirects: The maximum number of redirect responses that should be followed.
        transport: A transport class to use for sending requests over the network.
        app:An WSGI application to send requests to, rather than sending actual network requests.
        trust_env: Enables or disables usage of environment variables for configuration.
        default_encoding: The default encoding to use for decoding response text, if no charset information is included
            in a response Content-Type header. Set to a callable for automatic character set detection. Default:
            "utf-8".

    Examples:
    >>> import asyncio

    >>>> async with Client(auth=Auth(key="<your-tfl-api-key>")) as client:
    >>>     result = await client.get_lift_disruptions()
    >>>> print(result.data)
    """

    def __init__(
        self,
        *,
        auth: Auth | None = None,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        verify: VerifyTypes = True,
        cert: CertTypes | None = None,
        http1: bool = True,
        http2: bool = False,
        proxies: ProxiesTypes | None = None,
        mounts: Mapping[str, AsyncBaseTransport] | None = None,
        timeout: TimeoutTypes = DEFAULT_TIMEOUT_CONFIG,
        follow_redirects: bool = False,
        limits: Limits = DEFAULT_LIMITS,
        max_redirects: int = DEFAULT_MAX_REDIRECTS,
        event_hooks: Mapping[str, list[Callable[..., Any]]] | None = None,
        transport: AsyncBaseTransport | None = None,
        app: Callable[..., Any] | None = None,
        trust_env: bool = True,
        default_encoding: str | Callable[[bytes], str] = "utf-8",
    ) -> None:
        super().__init__(
            auth=auth,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            follow_redirects=follow_redirects,
            max_redirects=max_redirects,
            event_hooks=event_hooks,
            base_url="https://api.tfl.gov.uk",
            trust_env=trust_env,
            default_encoding=default_encoding,
            verify=verify,
            cert=cert,
            http1=http1,
            http2=http2,
            proxies=proxies,
            mounts=mounts,
            limits=limits,
            transport=transport,
            app=app,
        )

    async def get_lift_disruptions(self) -> Response:
        """Get lift disruptions.

        Gets all current lift disruptions for the current day.

        Returns:
            The response from the API as a `Response` model.
        """
        response = await self.get(url="Disruptions/Lifts/v2/")
        return Response(
            code=response.status_code, data=models.LiftDisruptionsV2ResponseModel.parse_obj(response.json())
        )
