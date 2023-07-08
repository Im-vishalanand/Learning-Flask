import json
from app import app

def test_get_all_weather():
    client = app.test_client()
    response = client.get('/weather')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert len(data) == 3

def test_get_weather_by_id():
    client = app.test_client()
    response = client.get('/weather/1')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert data['city'] == 'New York'

def test_get_weather_by_id_not_found():
    client = app.test_client()
    response = client.get('/weather/10')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert 'Weather data not found' in data['message']

# Add more tests for other CRUD operations...

if __name__ == '__main__':
    test_get_all_weather()
    test_get_weather_by_id()
    test_get_weather_by_id_not_found()
    # Call other test functions...
