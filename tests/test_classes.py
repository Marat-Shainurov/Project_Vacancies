import json


def test_hh_init(testing_instance_hh):
    """
    Тестирует инициализацию класса HH.
    """
    assert testing_instance_hh.area == 113
    assert testing_instance_hh.key_text == 'Python developer'


def test_hh_get_request(testing_instance_hh):
    """
    Тестирует работу метода get_request,
    проверяя наличие ожидаемого кол-ва объектов на одной странице.
    """
    response = testing_instance_hh.get_request()
    assert len(json.loads(response)['items']) == 100

def test_sj_init(testing_instance_sj):
    """
    Тестирует инициализацию класса HH.
    """
    assert testing_instance_sj.id == "v3.r.137452619.a63bcb7404a9e35b86138b7522ea580731285cad.4636fdc6cb7aa59a9a3960e3a42fd0d53b449a72"
    assert testing_instance_sj.key_text == 'Python developer'

def test_sj_get_request(testing_instance_sj):
    """
    Тестирует работу метода get_request,
    проверяя наличие общего ожидаемого кол-ва объектов.
    """
    assert len(testing_instance_sj.get_request()['objects']) == 500


# def test_pass_to_insert_hh():
#     pass
#
# def test_pass_to_insert_sj():
#     pass