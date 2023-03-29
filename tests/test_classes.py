import json


def test_hh_init(testing_instance_hh):
    """
    Тестирует инициализацию класса HH.
    """
    assert testing_instance_hh.area == 113
    assert testing_instance_hh.key_text == 'Python'


def test_hh_get_request(testing_instance_hh):
    """
    Тестирует работу метода get_request,
    проверяя наличие ожидаемого кол-ва объектов на странице.
    """
    response = testing_instance_hh.get_request()
    assert len(json.loads(response)['items']) == 100


def test_data_to_insert():
    pass
