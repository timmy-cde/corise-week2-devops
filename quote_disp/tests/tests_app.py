import pytest
from flask import url_for
import requests
import urllib

import sys, os
sys.path.append(os.path.join('..', 'quote_disp'))
from app import app

@pytest.fixture(scope='module')
def client():
    app.config.update({'TESTING': True})
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert 'healthy' in res.data.decode()

def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    assert "This is the Quote Display Service" in res.data.decode()


@pytest.fixture(scope='module')
def live_server_url(live_server):
    return live_server.url()

def test_get_quote_route(live_server_url):
    response = requests.get(f'{live_server_url}/get_quote')
    assert response.status_code == 200
    # assert response.text == 'This is a quote'

# @pytest.fixture('live_server')
# @pytest.mark.usefixtures('live_server')
# def test_response_from_another_port(live_server):
#     @live_server.app.route('/get_quote')
#     def test_endpoint():
#         return 'valid', 200
    
#     live_server.start()

#     res = urllib.urlopen(url_for('get_quote', _external=True))
    assert res.code == 200

    # url = live_server_url.replace(str(live_server_url.port), '5000')  # Replace the port with the desired port
    # response = requests.get(f"{url}/quote")
    # assert response.status_code == 200
