import pytest
from myapp import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_weather(client):
    response = client.get('/weather/San Francisco')
    assert response.status_code == 200
    assert response.json == {'temperature': 14, 'weather': 'Cloudy'}
    print("Test 'test_get_weather' passed.")

def test_get_weather_nonexistent_city(client):
    response = client.get('/weather/Nonexistent City')
    assert response.status_code == 404
    assert response.json == {'error': 'City not found'}
    print("Test 'test_get_weather_nonexistent_city' passed.")

def test_add_weather(client):
    data = {'city': 'Chicago', 'temperature': 18, 'weather': 'Cloudy'}
    response = client.post('/weather', json=data)
    assert response.status_code == 200
    assert response.json == {'message': 'Weather data added successfully'}
    print("Test 'test_add_weather' passed.")

def test_update_weather(client):
    data = {'temperature': 25, 'weather': 'Sunny'}
    response = client.put('/weather/Chicago', json=data)
    assert response.status_code == 200
    assert response.json == {'message': 'Weather data updated successfully'}
    print("Test 'test_update_weather' passed.")

def test_delete_weather(client):
    response = client.delete('/weather/Chicago')
    assert response.status_code == 200
    assert response.json == {'message': 'Weather data deleted successfully'}
    print("Test 'test_delete_weather' passed.")

if __name__ == '__main__':
    pytest.main()
