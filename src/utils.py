import json
import time
from src.classes import HH, SuperJob
from src.jobs_classes import HHVacancy, SJVacancy


def sorting(vacancies):
    """
    Сортирует список вакансий по ЗП. Анализируется значение коллекции 'salary' в каждой вакансии,
    и внутри вакансии создается новый элемент с ключом 'salary_to_be_sorted_by',
    на основе которого и производится сортировка.

    Значение для 'salary_to_be_sorted_by':
    Если 'salary' null - присваивается 0,
    Если указана не вилка from/to - присваивается имеющееся значение from,
    Если указана не вилка from/to, а значение int - присваивается имеющееся значение int,
    Если не указан from, но есть to - присваивается to, но дисконтируется на 0.75.
    """

    with open(vacancies, encoding='utf8') as f:
        content = f.read()
        content_new = f"[{content.strip().strip(',')}]"

    data = json.loads(content_new)
    currency_rate = 75

    for el in data:
        if el['salary'] is None:
            el['salary_to_be_sorted_by'] = 0
        elif isinstance(el['salary'], int):
            if el['salary']['currency'] in ['RUR', 'rub']:
                el['salary_to_be_sorted_by'] = el['salary']
            else:
                el['salary_to_be_sorted_by'] = el['salary'] * currency_rate
        elif el['salary']['from'] is None and el['salary']['to'] is not None:
            if el['salary']['currency'] in ['RUR', 'rub']:
                el['salary_to_be_sorted_by'] = round(el['salary']['to'] * 0.75)
            else:
                el['salary_to_be_sorted_by'] = el['salary']['to'] * 0.75 * currency_rate
        elif el['salary']['from'] == 0 and isinstance(el['salary']['to'], int):
            if el['salary']['currency'] in ['RUR', 'rub']:
                el['salary_to_be_sorted_by'] = round(el['salary']['to'] * 0.75)
            else:
                el['salary_to_be_sorted_by'] = round(el['salary']['to'] * 0.75 * currency_rate)
        else:
            if el['salary']['currency'] in ['RUR', 'rub']:
                el['salary_to_be_sorted_by'] = el['salary']['from']
            else:
                el['salary_to_be_sorted_by'] = el['salary']['from'] * currency_rate

    sorted_data = sorted(data, key=lambda x: x['salary_to_be_sorted_by'], reverse=True)

    return sorted_data


def get_top(vacancies, top_count):
    """
    Возвращает {top_count} записей из вакансий по зарплате.
    """

    sorted_array = sorting(vacancies)
    res = []
    count = 0

    iterator = iter(sorted_array)
    while count < top_count:
        try:
            item = next(iterator)
            count += 1
            res.append(item)
        except StopIteration:
            break

    return res


def write_to_file_final(top_to_apply, path_to_file):
    """
    Получает итоговый список из топ вакансий, готовых к записи в vacancies_to_apply.
    Создает экземпляры классов Vacancy и вызывает методы write_to_file.
    """

    for vacancy in top_to_apply:
        if vacancy['source'] == "HH":
            obj_hh = HHVacancy(vacancy)
            obj_hh.write_to_file(path_to_file)
        else:
            obj_sj = SJVacancy(vacancy)
            obj_sj.write_to_file(path_to_file)

def get_experience_from_user_input_hh(user_experience_hh: tuple):
    """
    Вспомогательная функция для функции get_started, конвертирующая простой ответ пользователя об опыте работы
    кандидата, в необходимый код параметра 'experience' для корректного request к API HH.
    """

    mapping = {'1': 'noExperience', '2': 'between1And3', '3': 'between3And6', '4': 'moreThan6'}
    user_experience_hh_fin = [mapping[el] for el in user_experience_hh]
    return tuple(user_experience_hh_fin)

def get_started():
    """
    Проводит интерактив с пользователем, получая текст запроса и ожидаемый опыт работы.
    Возвращает 2 экземпляра классов HH и SuperJob.
    """

    # Очистка файлов с данными и итоговыми рекомендациями вакансий, перед новыми реквестами
    with open('../src/response_data.json', 'w') as f:
        f.write("")
    with open('../src/vacancies_to_apply.txt', 'w') as f:
        f.write("")

    print("\nПривет!\nВведите текст по которому будет производится поиск на сайтах HH и SuperJob.")
    user_key_text = input("Ваш текст: ").strip()
    print("\nВыберете уровень ожидаемого опыта работы от кандидата на SuperJob.")
    print("\n'1' - опыт не требуется\n'2' - от 1 до 3 лет\n'3' - от 3 до  6 лет\n'4' - более 6 лет\n")
    print("Можно ввести несколько значений через пробел, для включения нескольких групп.")

    user_experience_sj = input("Введите опыт: ").strip()
    while not set(user_experience_sj.split(' ')).issubset({'1', '2', '3', '4'}):
        user_experience_sj = input("Введите опыт корректно: ").strip()

    user_experience_sj_fin = tuple(int(x) for x in set(user_experience_sj.split(' ')))

    print("\nВыберете уровень ожидаемого опыта работы от кандидата на HH по той же шкале. ")
    user_experience_hh = input("Введите опыт: ").strip()
    while not set(user_experience_hh.split(' ')).issubset({'1', '2', '3', '4'}):
        user_experience_hh = input("Введите опыт корректно: ").strip()

    user_experience_hh = tuple(x for x in set(user_experience_hh.split(' ')))
    user_experience_hh_fin = get_experience_from_user_input_hh(user_experience_hh)

    object_HH = HH(key_text=user_key_text, experience=user_experience_hh_fin)
    object_SJ = SuperJob(key_text=user_key_text, experience=user_experience_sj_fin)
    print("\nСпасибо, ожидайте загрузку инфо.")

    return object_HH, object_SJ
