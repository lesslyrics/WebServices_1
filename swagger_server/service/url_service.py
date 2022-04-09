import os
import tempfile

import shortuuid
from tinydb import TinyDB, Query
from tinydb.operations import delete

from tinydb.middlewares import CachingMiddleware
from functools import reduce
from shortuuid import *
import uuid
from swagger_server.models import ShortenedUrl

db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "urls.json")
url_db = TinyDB(db_file_path)


def add(url=None):
    queries = []
    query = Query()
    queries.append(query.original_url == url.original_url)
    query = reduce(lambda a, b: a & b, queries)
    res = url_db.search(query)
    if res:
        return 'Url already exists', 409

    # Generate unique url for length 7
    short_url = shortuuid.ShortUUID().random(length=7)
    url.url_id = str(uuid.uuid4())
    url.shortened_url = short_url
    url_db.insert(url.to_dict())
    return url.url_id


def get_by_id(url_id=None, newUrl=None):
    queries = []
    query = Query()
    queries.append(query.url_id == url_id)
    query = reduce(lambda a, b: a & b, queries)
    url = url_db.search(query)

    # url = url_db.get(doc_id=int(url_id))
    if not url:
        return 'not found', 404
    return url

def get_all():
    return url_db.all()


def update_by_id(url_id=None, new_url=None):
    queries = []
    query = Query()
    queries.append(query.url_id == url_id)
    query = reduce(lambda a, b: a & b, queries)
    url = url_db.search(query)

    # url = url_db.get(doc_id=int(url_id))
    if not url:
        return 'not found', 404

    ShortenedUrl = Query()
    url_db.update({'original_url': new_url.original_url, 'shortened_url': shortuuid.ShortUUID().random(length=7)}, ShortenedUrl.url_id == url_id)

    return url


def delete_by_id(url_id):
    ShortenedUrl = Query()
    student = url_db.get(ShortenedUrl.url_id == url_id)
    if not student:
        return 'not found', 404
    url_db.remove(ShortenedUrl.url_id == url_id)
    return url_id


def delete_all():
    url_db.drop_tables()
    return 'Delete successful'
