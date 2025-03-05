import unittest
from unittest.mock import patch
import requests

class TestAPI(unittest.TestCase):
    
    @patch('requests.post')
    def test_log_creation(self, mock_post):
        # Мокируем ответ от API
        mock_response = mock_post.return_value
        mock_response.status_code = 201
        
        response = requests.post('http://localhost:5000/api/logs', json={'message': 'Test log'})
        
        self.assertEqual(response.status_code, 201)
        mock_post.assert_called_once_with('http://localhost:5000/api/logs', json={'message': 'Test log'})

    @patch('requests.post')
    def test_notification(self, mock_post):
        # Мокируем ответ от API
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        
        response = requests.post('http://localhost:5001/api/notify', json={'message': 'Test notification'})
        
        self.assertEqual(response.status_code, 200)
        mock_post.assert_called_once_with('http://localhost:5001/api/notify', json={'message': 'Test notification'})

if __name__ == "__main__":
    unittest.main()
