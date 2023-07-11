import pytest
from myapp import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# def test_get_weather(client):
#     response = client.get('/weather/San Francisco')
#     assert response.status_code == 200
#     assert response.json == {'temperature': 14, 'weather': 'Cloudy'}

#     response = client.get('/weather/New York')
#     assert response.status_code == 200
#     assert response.json == {'temperature': 20, 'weather': 'Sunny'}

#     response = client.get('/weather/Los Angeles')
#     assert response.status_code == 200
#     assert response.json == {'temperature': 24, 'weather': 'Sunny'}

#     response = client.get('/weather/Seattle')
#     assert response.status_code == 200
#     assert response.json == {'temperature': 10, 'weather': 'Rainy'}

#     response = client.get('/weather/Austin')
#     assert response.status_code == 200
#     assert response.json == {'temperature': 32, 'weather': 'Hot'}

#     response = client.get('/weather/Nonexistent City')
#     assert response.status_code == 404
#     assert response.json == {'error': 'City not found'}

#     print("All tests Passed")

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


if __name__ == '__main__':
    pytest.main()