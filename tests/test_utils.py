from src.utils import sorting, get_top, write_to_file_final


def test_sorting():
    """
    Тестирует сортировку и наличие изменений в порядке расположения элементов в тестовом файле.
    """
    path_to_file = "C:\\Users\\m_sha\\PycharmProjects\\Project_Vacancies\\src\\test_response_data.json"
    sorted_data = sorting(path_to_file)
    assert sorted_data[0]['salary'] == {"from": 1000000, "to": 1500000, "currency": "rub"}


def test_get_top():
    """
    Тестирует подбор 2 элементов, применив метод get_top.
    """
    path_to_file = "C:\\Users\\m_sha\\PycharmProjects\\Project_Vacancies\\src\\test_response_data.json"
    processed_array = get_top(path_to_file, 2)
    assert processed_array[1]['salary'] == {"from": 1000, "to": 2000, "currency": "USD", "gross": False}


def test_write_to_file():
    """
    Тестирует факт записи данных в файл при вызове функции write_to_file_final.
    """
    data_to_write = get_top("C:\\Users\\m_sha\\PycharmProjects\\Project_Vacancies\\src\\test_response_data.json", 2)
    testing_file_path = "C:\\Users\\m_sha\\PycharmProjects\\Project_Vacancies\\tests\\test_vacancies_to_apply.txt"
    write_to_file_final(data_to_write, testing_file_path)
    with open(testing_file_path, encoding='utf8') as f:
        content = f.read()
    assert content[0] == "\n"
    with open(testing_file_path, 'w', encoding='utf8') as f:
        f.write('')
