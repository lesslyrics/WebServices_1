# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.shortened_url import ShortenedUrl  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_id_delete(self):
        """Test case for id_delete

        Delete shortened id
        """
        response = self.client.open(
            '/AlinaBoshchenko/tester/1.0.0/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_id_get(self):
        """Test case for id_get

        Redirect to Original Url
        """
        response = self.client.open(
            '/AlinaBoshchenko/tester/1.0.0/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_id_put(self):
        """Test case for id_put

        Update Url
        """
        response = self.client.open(
            '/AlinaBoshchenko/tester/1.0.0/{id}'.format(id='id_example'),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_root_delete(self):
        """Test case for root_delete

        Delete all keys
        """
        response = self.client.open(
            '/AlinaBoshchenko/tester/1.0.0/',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_root_get(self):
        """Test case for root_get

        Get all keys
        """
        response = self.client.open(
            '/AlinaBoshchenko/tester/1.0.0/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_root_post(self):
        """Test case for root_post

        Generate shortened url
        """
        body = ShortenedUrl()
        response = self.client.open(
            '/AlinaBoshchenko/tester/1.0.0/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
