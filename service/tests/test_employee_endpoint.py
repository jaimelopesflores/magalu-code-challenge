import unittest
import sys
from subprocess import call
from time import sleep

sys.path.append('../')

from app import app

class EmployeeEndpointTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        command = 'docker run -d -p 27999:27017 --name MAGALU_CODE_CHALLENGE_MONGO mongo'
        call(command.split(' '))
        sleep(5)

    @classmethod
    def tearDownClass(cls):
        command = 'docker rm -f MAGALU_CODE_CHALLENGE_MONGO'
        call(command.split(' '))

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all(self):
        result = self.app.get('/employee')
        self.assertEqual(result.status_code, 200)

    def test_create(self):
        payload = {
            "department": "sales",
            "email": "sundar-pichai@magalu.com",
            "name": "Sundar Pichai"
        }
        result = self.app.post('/employee', json=payload)
        self.assertEqual(result.status_code, 200)
