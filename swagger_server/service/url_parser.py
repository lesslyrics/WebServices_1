import re
from urllib.parse import urlparse


def is_valid_URL(url):
    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    p = re.compile(regex)

    if url is None:
        return False

    if re.search(p, url):
        return True
    else:
        return False


def is_valid_URL_alternative(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False