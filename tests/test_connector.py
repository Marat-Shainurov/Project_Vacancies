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
    assert os.path.exists(f"../src/{file_name}") is False
    obj = Connector(file_name)
    assert os.path.exists(obj.path_to_file) is True
    assert obj.data_file == file_name
    obj.data_file = 'test_insert.json'
    assert os.path.exists(obj.path_to_file) is True
    assert obj.data_file == 'test_insert.json'
    os.remove(obj.path_to_file)
    os.remove(f"../src/{file_name}")


def test_select(testing_instance_connector_example):
    assert testing_instance_connector_example.select({'source': 'HH'})[0]['name'] == "ML-специалист (Junior)"
    assert testing_instance_connector_example.select({'invalid_key': 1}) is None


def test_delete():
    """
    Тестирует удаление элемента из файла.
    Для этого создается временный тестовый объект класса с тестовым временным файлом.
    Во временный файл записывается инфо из test_response_data.json.
    Далее из временного файла удаляется с помощью метода test_delete(),
    и проверяется наличие изменение данных (изменение длины списка и данные в первом элементе).
    """

    obj = Connector('testing.json')
    with open(obj.path_to_file, 'w', encoding='utf8') as f:
        with open("../src/test_response_data.json", encoding='utf8') as file:
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

def test_insert_hh():
    """
    Тестирует работу метода insert_hh() класса Connector, временно создавая экземпляр класса и файл,
    записывая инфо тестового массива.
    """

    array_to_test = {
        'items': [{'id': 'some_id', 'name': 'some_name', 'salary': 'some_salary','alternate_url': 'some_alternate_url',
                   'employer': {'name': 'some_name'}, 'snippet': 'some_snippet'}]}

    obj = Connector('test_insert_hh.json')
    obj.insert_hh(array_to_test)

    with open(obj.path_to_file, encoding='utf8') as f:
        content = f.read()
        content_new = f"[{content.strip().strip(',')}]"
    data = json.loads(content_new)
    assert data[0]['id'] == 'some_id'
    os.remove(obj.path_to_file)


def test_insert_sj():
    """
    Тестирует работу метода insert_sj() класса Connector, временно создавая экземпляр класса и файл,
    записывая инфо тестового массива.
    """

    array_to_test = {
        'objects': [{'id': 'some_id', 'profession': 'some_name', 'payment_from': 'some_salary', 'payment_to': 'some_salary',
                     'currency': 'some_salary', 'link': 'some_alternate_url', 'firm_name': 'some_name', 'work': 'some_descr'}]}

    obj = Connector('test_insert_sj.json')
    obj.insert_sj(array_to_test)

    with open(obj.path_to_file, encoding='utf8') as f:
        content = f.read()
        content_new = f"[{content.strip().strip(',')}]"
    data = json.loads(content_new)
    assert data[0]['employer'] == 'some_name'
    os.remove(obj.path_to_file)
