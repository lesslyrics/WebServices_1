# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ShortenedUrl(Model):
    def __init__(self, url_id: str=None, original_url: str=None, shortened_url: str=None):  # noqa: E501
        """
        :param url_id: The url_id of this ShortenedUrl.  # noqa: E501
        :type url_id: str
        :param original_url: The original_url of this ShortenedUrl.  # noqa: E501
        :type original_url: str
        :param shortened_url: The shortened_url of this ShortenedUrl.  # noqa: E501
        :type shortened_url: str
        """
        self.swagger_types = {
            'url_id': str,
            'original_url': str,
            'shortened_url': str
        }

        self.attribute_map = {
            'url_id': 'url_id',
            'original_url': 'originalUrl',
            'shortened_url': 'shortenedUrl'
        }
        self._url_id = url_id
        self._original_url = original_url
        self._shortened_url = shortened_url

    @classmethod
    def from_dict(cls, dikt) -> 'ShortenedUrl':
        """Returns the dict as a model
        :param dikt: A dict.
        :type: dict
        :return: The ShortenedUrl of this ShortenedUrl.  # noqa: E501
        :rtype: ShortenedUrl
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url_id(self) -> str:
        """Gets the url_id of this ShortenedUrl.


        :return: The url_id of this ShortenedUrl.
        :rtype: str
        """
        return self._url_id

    @url_id.setter
    def url_id(self, url_id: str):
        """Sets the url_id of this ShortenedUrl.


        :param url_id: The url_id of this ShortenedUrl.
        :type url_id: str
        """

        self._url_id = url_id

    @property
    def original_url(self) -> str:
        """Gets the original_url of this ShortenedUrl.

        Valid URL thah should be shortened.  # noqa: E501

        :return: The original_url of this ShortenedUrl.
        :rtype: str
        """
        return self._original_url

    @original_url.setter
    def original_url(self, original_url: str):
        """Sets the original_url of this ShortenedUrl.

        Valid URL thah should be shortened.  # noqa: E501

        :param original_url: The original_url of this ShortenedUrl.
        :type original_url: str
        """
        if original_url is None:
            raise ValueError("Invalid value for `original_url`, must not be `None`")  # noqa: E501

        self._original_url = original_url

    @property
    def shortened_url(self) -> str:
        """Gets the shortened_url of this ShortenedUrl.

        Valid URL thah should be shortened.  # noqa: E501

        :return: The shortened_url of this ShortenedUrl.
        :rtype: str
        """
        return self._shortened_url

    @shortened_url.setter
    def shortened_url(self, shortened_url: str):
        """Sets the shortened_url of this ShortenedUrl.

        Valid URL thah should be shortened.  # noqa: E501

        :param shortened_url: The shortened_url of this ShortenedUrl.
        :type shortened_url: str
        """

        self._shortened_url = shortened_url