import pytest
from src.classes import Engine, HH, SuperJob
from src.connector import Connector


@pytest.fixture
def testing_instance_hh():
    obj = HH()
    return obj


@pytest.fixture
def testing_instance_connector():
    obj = Connector('response_data.json')
    return obj
