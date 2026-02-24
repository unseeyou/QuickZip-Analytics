from urllib.parse import urlparse
from flask import request

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(target)
    return (
        test_url.scheme in ("http", "https")
        and ref_url.netloc == test_url.netloc
        or not test_url.netloc
    )
