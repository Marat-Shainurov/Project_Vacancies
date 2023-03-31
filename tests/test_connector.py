from src.connector import Connector
import os
import json


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
    assert os.path.exists(f"C:\\Users\\m_sha\\PycharmProjects\\Project_Vacancies\\src\\{file_name}") is False
    obj = Connector(file_name)
    assert os.path.exists(f"C:\\Users\\m_sha\\PycharmProjects\\Project_Vacancies\\src\\{file_name}") is True
    assert obj.data_file == file_name
    obj.data_file = 'new.json'
    assert os.path.exists(f"C:\\Users\\m_sha\\PycharmProjects\\Project_Vacancies\\src\\{'new.json'}") is True
    assert obj.data_file == 'new.json'
    os.remove(f"C:\\Users\\m_sha\\PycharmProjects\\Project_Vacancies\\src\\{'new.json'}")
    os.remove(f"C:\\Users\\m_sha\\PycharmProjects\\Project_Vacancies\\src\\{file_name}")

def test_select(testing_instance_connector_example):
    assert testing_instance_connector_example.select({'source': 'HH'})[0]['name'] == "ML-специалист (Junior)"
    assert testing_instance_connector_example.select({'invalid_key': 1}) is None

def test_delete():

    obj = Connector('testing.json')
    with open(obj.path_to_file, 'w', encoding='utf8') as f:
        with open('../tests/test_response_data.json', encoding='utf8') as file:
            content = file.read()
        f.write(content)
    obj.delete({'source': 'HH'})

    with open(obj.path_to_file, encoding='utf8') as f:
        content = f.read()
        content_new = f"[{content.strip().strip(',')}]"
    data = json.loads(content_new)

    assert data[0]['name'] == "Специалист службы поддержки (с техническими знаниями)"
    assert len(data) == 2

    os.remove(obj.path_to_file)
