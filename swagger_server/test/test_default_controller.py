# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.shortened_url import ShortenedUrl  # noqa: E501
from swagger_server.test import BaseTestCase


class TestController(BaseTestCase):

    base_path = 'http://localhost:8080/'
    example_id = '5a1f7a7e-92c0-4268-854f-9760606067fd'

    def test_root_delete(self):
        """Test case for root_delete
        Delete all keys
        """
        response = self.client.open(
            self.base_path,
            method='DELETE')
        print("Response: " + response.data.decode('utf-8'))
        self.assert404(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_root_post(self):
        """Test case for root_post
        Generate shortened url
        """
        body = ShortenedUrl(original_url="https://google.com")
        response = self.client.open(
            self.base_path,
            method='POST',
            data=json.dumps(body),
            content_type='application/json')

        example_id = response.data.decode('utf-8').replace("\"", "")
        print("Response: " + example_id)
        self.assertStatus(response, 201, 'Response body is: ' + example_id)

        body = ShortenedUrl(original_url="https://gmail.com")
        response = self.client.open(
            self.base_path,
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        example_id = response.data.decode('utf-8').replace("\"", "")
        print("Response: " + example_id)
        self.assertStatus(response, 201, 'Response body is: ' + example_id)

    def test_invalid_url(self):
        """Test case for invalid url
            """
        body = ShortenedUrl(original_url="https/google.com")
        response = self.client.open(
            self.base_path,
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        print("Response: " + response.data.decode('utf-8').replace("\"", ""))
        self.assertStatus(response, 400, 'Response body is : ' + response.data.decode('utf-8').replace("\"", ""))

    def test_existing_url(self):
        """Test case for existing url
            """
        body = ShortenedUrl(original_url="https://google.com")
        response = self.client.open(
            self.base_path,
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        print(response.data.decode('utf-8').replace("\"", ""))
        self.assertStatus(response, 409, 'Response body is: ' + (response.data.decode('utf-8').replace("\"", "")))

    def test_root_get(self):
        """Test case for root_get
        Get all keys
        """
        response = self.client.open(
            self.base_path,
            method='GET')
        print(response.data.decode('utf-8').replace("\"", ""))
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))
        return response.data.decode('utf-8').replace("\"", "")

    def test_id_delete(self):
        """Test case for id_delete
        Delete shortened id
        """

        print("Id to delete: " + self.example_id)
        response = self.client.open(
            (self.base_path + '{id}').format(id=self.example_id),
            method='DELETE')
        print(response.data.decode('utf-8').replace("\"", ""))
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_non_existing_id_delete(self):
            """Test case for id_delete
            Delete shortened id
            """
            non_example_id = '0'

            print("Id to delete: " + non_example_id)
            response = self.client.open(
                (self.base_path + '{id}').format(id=non_example_id),
                method='DELETE')
            print(response.data.decode('utf-8').replace("\"", ""))
            self.assert404(response, 'Response body is : ' + response.data.decode('utf-8'))

    def test_id_get(self):
        """Test case for id_get
        Redirect to Original Url
        """
        response = self.client.open(
            (self.base_path + '{id}').format(id=self.example_id),
            method='GET')
        print(response.data.decode('utf-8').replace("\"", ""))
        self.assertStatus(response, 301, 'Response body is : ' + response.data.decode('utf-8'))

    def test_id_put(self):
        """Test case for id_put
        Update Url
        """
        body = ShortenedUrl(original_url="https://g3le.com")

        response = self.client.open(
            (self.base_path + '{id}').format(id=self.example_id),
            data=json.dumps(body),
            content_type='application/json',
            method='PUT')
        print(response.data.decode('utf-8').replace("\"", ""))
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
