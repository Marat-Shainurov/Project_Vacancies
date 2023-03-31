from src.utils import sorting, get_top, write_to_file_final


def test_sorting():
    path_to_file = f"../tests/test_response_data.json"
    sorted_data = sorting(path_to_file)
    assert sorted_data[0]['salary'] == {"from": 1000000, "to": 1500000, "currency": "rub"}


def test_get_top():
    path_to_file = f"../tests/test_response_data.json"
    processed_array = get_top(path_to_file, 2)
    assert processed_array[1]['salary'] == {"from": 1000, "to": 2000, "currency": "USD", "gross": False}


def test_write_to_file():
    data_to_write = get_top(f"../tests/test_response_data.json", 2)
    write_to_file_final(data_to_write, f"../tests/test_vacancies.txt")
    with open(f"../tests/test_vacancies.txt", encoding='utf8') as f:
        content = f.read()
    assert content[0] == "\n"
    with open(f"../tests/test_vacancies.txt", 'w', encoding='utf8') as f:
        f.write('')
