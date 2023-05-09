"""Client to interact with the air quality API."""

from typing import Any, Callable, List, Mapping, Optional, Union

import httpx
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

from tfl.clients import Auth, TFLClient

__all__ = ["AirQualityClient"]


class AirQualityClient(TFLClient):
    """Client to interact with the air quality API.

    [API reference](https://api-portal.tfl.gov.uk/api-details#api=AirQuality&operation=AirQuality_Get)

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

    Example:
        ```python
        from tfl.clients import Auth


        async with AirQualityClient(auth=Auth(key="<your-tfl-api-key>")) as client:
            response = await client.get_air_quality()

        print(response.json())
        ```
    """

    def __init__(
        self,
        *,
        auth: Optional[Auth] = None,
        params: Optional[QueryParamTypes] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        verify: VerifyTypes = True,
        cert: Optional[CertTypes] = None,
        http1: bool = True,
        http2: bool = False,
        proxies: Optional[ProxiesTypes] = None,
        mounts: Optional[Mapping[str, AsyncBaseTransport]] = None,
        timeout: TimeoutTypes = DEFAULT_TIMEOUT_CONFIG,
        follow_redirects: bool = False,
        limits: Limits = DEFAULT_LIMITS,
        max_redirects: int = DEFAULT_MAX_REDIRECTS,
        event_hooks: Optional[Mapping[str, List[Callable[..., Any]]]] = None,
        transport: Optional[AsyncBaseTransport] = None,
        app: Optional[Callable[..., Any]] = None,
        trust_env: bool = True,
        default_encoding: Union[str, Callable[[bytes], str]] = "utf-8",
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

    async def get_air_quality(self) -> httpx.Response:
        """Gets current air quality data feed.

        Returns:
            The response from the API.
        """
        return await self.get(url=f"/AirQuality")
