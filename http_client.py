import httpx
from typing import Optional, Dict, Any, Tuple

class AcmeHTTPClient:
    USER_AGENT = "AcmeHTTPClient/1.0"

    def __init__(
        self,
        base_url: Optional[str] = None,
        timeout: Optional[float] = 10.0,
        headers: Optional[Dict[str, str]] = None,
        follow_redirects: bool = False,
        mtls_cert: Optional[Tuple[str, str]] = None,
        ca_cert: Optional[str] = None,
    ):
        default_headers = {"User-Agent": self.USER_AGENT}
        if headers:
            default_headers.update(headers)

        self._client: httpx.Client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            headers=default_headers,
            follow_redirects=follow_redirects,
            cert=mtls_cert,
            verify=ca_cert if ca_cert else True,
        )

    def close(self):
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def get(self, url: str, **kwargs: Any) -> httpx.Response:
        return self._client.get(url, **kwargs)

    def post(self, url: str, **kwargs: Any) -> httpx.Response:
        return self._client.post(url, **kwargs)

    def put(self, url: str, **kwargs: Any) -> httpx.Response:
        return self._client.put(url, **kwargs)

    def patch(self, url: str, **kwargs: Any) -> httpx.Response:
        return self._client.patch(url, **kwargs)

    def delete(self, url: str, **kwargs: Any) -> httpx.Response:
        return self._client.delete(url, **kwargs)
