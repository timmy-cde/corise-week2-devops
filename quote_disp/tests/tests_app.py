import pytest
from flask import url_for
import requests
import urllib

import sys, os
sys.path.append(os.path.join('..', 'quote_disp'))
from app import app

@pytest.fixture()
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
