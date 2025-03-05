import unittest
import requests

class TestAPI(unittest.TestCase):
    
    def test_log_creation(self):
        response = requests.post('http://localhost:5000/api/logs', json={'message': 'Test log'})
        self.assertEqual(response.status_code, 201)

    def test_notification(self):
        response = requests.post('http://localhost:5001/api/notify', json={'message': 'Test notification'})
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
