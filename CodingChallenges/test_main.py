import unittest
from flask import Flask, url_for
from main import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # creating the test client
        self.app = app.test_client()

    #testing the default path
    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Main Page', response.data)

    #testing the learning path
    def test_learning_paths_route(self):
        response = self.app.get('/learning_paths')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Learning Paths', response.data)
        self.assertIn(b'Beginner Route', response.data)
        self.assertIn(b'Intermediate Route', response.data)
        self.assertIn(b'Advanced Route', response.data)


if __name__ == '__main__':
    unittest.main()
