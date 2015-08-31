import sys
import os
from unittest import TestCase
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from app import create_app

class TestSubscriptionsRoutes(TestCase):
    '''
    Tests the subscriptions routes

    Before you execute these tests, you need to start the server on port 5000
    '''

    def setUp(self):
        self.app = create_app('DEVELOPMENT') 
        self.context = self.app.app_context()
        self.client = self.app.test_client()
        self.context.push()

    def tearDown(self):
        self.context.pop()

    def test_messages(self):
        payload = {"message": "This is a test message"}
        res = self.client.post("/messages/add", data=payload)
        self.assertEqual(res.mimetype, "application/json")
        self.assertEqual(res.status, "200 OK")
        self.assertEqual(res.get_data(), '{"server_resp": "Success"}')
