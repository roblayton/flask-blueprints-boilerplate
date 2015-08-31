import sys
import os
from unittest import TestCase
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from app import create_app


class TestRootRoutes(TestCase):
    '''
    Tests the root level routes

    Before you execute these tests, you need to start the server on port 5000
    '''

    def setUp(self):
        self.app = create_app('DEVELOPMENT') 
        self.context = self.app.app_context()
        self.client = self.app.test_client()
        self.context.push()

    def tearDown(self):
        self.context.pop()

    def test_routes(self):
        res = self.client.get('/')
        self.assertEqual(res.status, "200 OK")
