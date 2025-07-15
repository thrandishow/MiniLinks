import string
import secrets

SHORT_URL_LENGTH = 6


def generate_short_url(length: int = SHORT_URL_LENGTH) -> str:
    characters = string.ascii_letters + string.digits
    while True:
        short_url = "".join(secrets.choice(characters) for _ in range(length))
        if short_url not in url_map:
            return short_url
