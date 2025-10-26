#Aqui va todo el testing de los endpoints y Javascripts
import pytest as pt
from app import app as flask_app

@pt.fixture
def app():
    flask_app.config['TESTING'] = True
    yield flask_app


@pt.fixture
def client(app):
    return app.test_client()
