import requests
import pytest
from faker import Faker 

fake = Faker()

@pytest.mark.parametrize("resource_id", [1, 5])
def test_get_resource(api_base_url, resource_id):
    url = f"{api_base_url}/posts/{resource_id}"
    response = requests.get(url)
    data = response.json()
    
    assert response.status_code == 200, f"FAIL: Esperado 200, obtenido {response.status_code}"
    assert data['id'] == resource_id, "FAIL: El ID del recurso devuelto no coincide."
    assert isinstance(data['userId'], int), "FAIL: El campo 'userId' no es un entero."
    

def test_post_create_resource(api_base_url):
    url = f"{api_base_url}/posts"
    payload = {"title": fake.catch_phrase(), "body": "contenido de prueba", "userId": 1}
    
    response = requests.post(url, json=payload)
    data = response.json()
    
    assert response.status_code == 201, f"FAIL: Esperado 201, obtenido {response.status_code}"
    assert 'id' in data, "FAIL: El recurso creado no devolvió un ID."
    assert data['title'] == payload['title'], "FAIL: El título devuelto no coincide."
    

def test_delete_resource(api_base_url):
    url = f"{api_base_url}/posts/1"
    response = requests.delete(url)
    
    assert response.status_code == 200, f"FAIL: Esperado 200, obtenido {response.status_code}"
