import pytest
from src.classes import Engine, HH, SuperJob
from src.connector import Connector


@pytest.fixture
def testing_instance_hh():
    obj = HH(key_text="Python", area=113, experience="noExperience")
    return obj


@pytest.fixture
def testing_instance_connector():
    obj = Connector('response_data.json')
    return obj


@pytest.fixture
def testing_instance_sj():
    obj = SuperJob(key_text='Python', area=1, experience=1)
    return obj
