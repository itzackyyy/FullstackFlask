def test_index_route(client):
    response = client.get('/login')
    assert response.status_code == 200

    if response.status_code == 200:
        print("Ha funcionao")


def test_registrar_route(client):
    response = client.get('/registrar')
    assert response.status_code == 200
    if response.status_code == 200:
        print("Ha funcionao")