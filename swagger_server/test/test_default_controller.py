# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_addition_get(self):
        """Test case for addition_get

        
        """
        query_string = [('x', 3.4),
                        ('y', 3.4)]
        response = self.client.open(
            '/addition',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_division_get(self):
        """Test case for division_get

        
        """
        query_string = [('x', 3.4),
                        ('y', 3.4)]
        response = self.client.open(
            '/division',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_multiplication_get(self):
        """Test case for multiplication_get

        
        """
        query_string = [('x', 3.4),
                        ('y', 3.4)]
        response = self.client.open(
            '/multiplication',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_substraction_get(self):
        """Test case for substraction_get

        
        """
        query_string = [('x', 3.4),
                        ('y', 3.4)]
        response = self.client.open(
            '/substraction',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
