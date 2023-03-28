import pytest
from src.classes import Engine, HH, SuperJob
from src.connector import Connector


@pytest.fixture
def testing_instance_hh():
    obj = HH()
    return obj
