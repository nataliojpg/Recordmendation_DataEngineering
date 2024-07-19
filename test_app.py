import requests

def test_recom():
    url = 'http://localhost:8000/recommend'  
    data = {'cancion': 'Tangerine', 'artista': 'Led Zeppelin'} 
    response = requests.post(url, json=data)
    print("Recomendaciones enviadas")
    assert response.status_code == 200
    assert 'recommendations' in response.json()

if __name__ == "__main__":
    test_recom()