import os
import tempfile

import shortuuid
from tinydb import TinyDB, Query
from flask import Flask, redirect
from functools import reduce
from shortuuid import *
import uuid
from swagger_server.service.url_parser import is_valid_URL

db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "urls.json")
url_db = TinyDB(db_file_path)


def add(url=None):

    if not is_valid_URL(url.original_url):
        return 'Invalid Url', 400

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


def redirect_to_full_by_id(url_id=None):
    queries = []
    query = Query()
    queries.append(query.url_id == url_id)
    query = reduce(lambda a, b: a & b, queries)
    url = url_db.search(query)

    if not url:
        return 'not found', 404
    return redirect(url[0]['original_url'], code=301)


def get_all():
    return url_db.all()

# TODO: mention in the report alternative way of validation

def update_by_id(url_id=None, new_url=None):
    queries = []
    query = Query()
    queries.append(query.url_id == url_id)
    query = reduce(lambda a, b: a & b, queries)
    url = url_db.search(query)

    # url = url_db.get(doc_id=int(url_id))
    if not url:
        return 'Not found', 404

    if not is_valid_URL(new_url.original_url):
        return 'Invalid Url', 400

    shortened_url = Query()
    url_db.update({'original_url': new_url.original_url, 'shortened_url': shortuuid.ShortUUID().random(length=7)}, shortened_url.url_id == url_id)

    return url


def delete_by_id(url_id):
    ShortenedUrl = Query()
    student = url_db.get(ShortenedUrl.url_id == url_id)
    if not student:
        return 'Not found', 404
    url_db.remove(ShortenedUrl.url_id == url_id)
    return url_id


def delete_all():
    url_db.drop_tables()
    return 'Delete successful'
