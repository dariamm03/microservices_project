import requests

def test_log_creation():
    response = requests.post('http://localhost:5000/api/logs', json={'message': 'Test log'})
    assert response.status_code == 201

def test_notification():
    response = requests.post('http://localhost:5001/api/notify', json={'message': 'Test notification'})
    assert response.status_code == 200

if __name__ == "__main__":
    test_log_creation()
    test_notification()
    print("All tests passed!")
