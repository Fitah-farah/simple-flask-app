import unittest
from app import app  # Import the app from your application file

class TestApp(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.client = app.test_client()

    def test_home(self):
        # Make a GET request to the root URL
        response = self.client.get('/')
        self.assertEqual(response.data, b'Hello, World from ECS!')  # Check if the response matches

if __name__ == '__main__':
    unittest.main()
