import unittest
import time
import requests
import importlib

PORT = 8000

class TestPingServer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server_module = importlib.import_module('ping')
        cls.server = cls.server_module.HTTPServer(("", PORT), cls.server_module.CustomHTTPRequestHandler)
        cls.server_thread = cls.server.serve_forever()  # Start the server

        time.sleep(1)  # Give the server time to start

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()  # Gracefully shut down the server

    def test_ping(self):
        response = requests.get(f'http://localhost:{PORT}/ping')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/plain', response.headers['Content-Type'])
        self.assertEqual(response.text, 'Found it!!')

    def test_not_found(self):
        response = requests.get(f'http://localhost:{PORT}/notfound')
        self.assertEqual(response.status_code, 404)
        self.assertIn('text/plain', response.headers['Content-Type'])
        self.assertEqual(response.text, 'Not Found')

if __name__ == "__main__":
    unittest.main()
