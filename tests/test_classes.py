import json


def test_hh_init(testing_instance_hh):
    assert testing_instance_hh.area == 113
    assert testing_instance_hh.key_text == 'Python'


def test_hh_get_request(testing_instance_hh):
    response = testing_instance_hh.get_request()
    assert len(json.loads(response)['items']) == 100


def test_data_to_insert():
    pass
