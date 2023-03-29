from src.connector import Connector
import os


def test_init_connector(testing_instance_connector):
    """
    Тестирует инициализацию класса Connector.
    """
    assert testing_instance_connector.data_file == 'response_data.json'

def test_init_connector_no_file():
    """
    Тестирует создание нового экземпляра класса, и присвоение значения атрибуту data_file несуществующего на момент
    инициализации значения.
    Ожидания - создаются новые файлы и экземпляры класса Connector с новым значением data_file.
    """
    file_name = 'non_existing_file.json'
    assert os.path.exists(f"../src/{file_name}") is False
    obj = Connector(file_name)
    assert os.path.exists(f"../src/{file_name}") is True
    assert obj.data_file == file_name
    obj.data_file = 'new.json'
    assert os.path.exists(f"../src/new.json") is True
    assert obj.data_file == 'new.json'
