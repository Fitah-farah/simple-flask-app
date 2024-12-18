import unittest
from app import app  # Assuming your Flask app is in app.py

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)  # Adjust based on your app's response

if __name__ == '__main__':
    unittest.main()
