import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.shortened_url import ShortenedUrl  # noqa: E501
from swagger_server import util
from swagger_server.service.url_service import *


def id_delete(url_id):  # noqa: E501
    """Delete shortened id

    :param url_id:
    :type url_id: str

    :rtype: None
    """
    return  delete_by_id(url_id)


def id_get(url_id):  # noqa: E501
    """Redirect to Original Url

    Redirect and count number of redirections. # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return redirect_to_full_by_id(url_id)


def id_put(body, url_id):  # noqa: E501
    """Update Url

    :param id: 
    :type id: str

    :rtype: None
    """

    if connexion.request.is_json:
        body = ShortenedUrl.from_dict(connexion.request.get_json())
        return update_by_id(url_id, body)
    return 500, 'error'


def root_delete():  # noqa: E501
    """Delete all keys
    :rtype: None
    """
    return delete_all()


def root_get():  # noqa: E501
    """Get all keys
    :rtype: List[ShortenedUrl]
    """
    return get_all()


def root_post(body):  # noqa: E501
    """Generate shortened url

     # noqa: E501

    :param body: A JSON object containing URL information
    :type body: dict | bytes

    :rtype: ShortenedUrl
    """
    if connexion.request.is_json:
        body = ShortenedUrl.from_dict(connexion.request.get_json())
        return add(body)
    return 500, 'error'
