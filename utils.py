import hashlib
import validators
from datetime import datetime
import re

def generate_short_url(long_url):
    # Generate a short URL using a hash of the long URL.
    return hashlib.md5(long_url.encode()).hexdigest()[:7]

def is_valid_url(url:str)->bool:
    """Check if the provided URL is valid."""
    return validators.url(url)

# def is_valid_url(url: str) -> bool:
#     """Validate the URL."""
#     regex = re.compile(
#         r'^(https?://)?'  # http:// or https://
#         r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'  # Domain
#         r'(/.*)?$'  # Optional path
#     )
#     return re.match(regex, url) is not None


