import json
import requests
import time


def print_info(object_to_print) -> str:
    """
    Вспомогательный статичный метод, для поиска нужной инфо в коллекциях, для создания методов и атрибутов.
    Печатает коллекцию в удобном для чтения формате.
    """
    res = json.dumps(object_to_print, indent=2, ensure_ascii=False)
    return res


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass


# шаблон запросов к API HH and SuperJob

def get_page(page=0):
    """
    Метод для получения страницы со списком вакансий
    page - страницы начинается с 0 (с первой страницы).
    """

    # справочник для параметров запроса
    params = {
        'text': 'NAME:Python',  # текст фильтра, в имени должно быть Python
        'area': 1,  # код локацииб 1 - Мск
        'page': page,  # индекс страницы
        'per_page': 100  # кол-во вакансий на 1 странице
    }

    req = requests.get('https://api.hh.ru/vacancies', params)  # Запрос к AIP
    data = req.content.decode()  # Декодирует, чтобы кириллица отображалась корректно
    req.close()

    return data


js_objs = []

for page in range(0, 5):
    js_obj = json.loads(get_page(page))  # Преобразовывает текст ответа в словарь Python
    js_objs.extend(js_obj['items'])  # Добавляет текущий ответ в js_objs

    if (js_obj['pages'] - page) <= 1:  # Проверка на последнюю страницу, если вакансий меньше 2000
        break
    time.sleep(0.25)

count = 0
for i in js_objs:
    print(i)
    count += 1


def get_page_SJ(page=0):
    params = {
        'keyword': 'Python, Developer, Разработчик',
        'town': 'Москва', 'page': page, 'count': 100}
    headers = {
        "X-Api-App-Id": "v3.r.137452619.a63bcb7404a9e35b86138b7522ea580731285cad.4636fdc6cb7aa59a9a3960e3a42fd0d53b449a72"}
    req = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)  # Запрос к AIP
    data = req.content.decode()  # Декодирует, чтобы кириллица отображалась корректно
    req.close()

    return data


js_objs_SJ = []

for page in range(0, 3):
    js_obj = json.loads(get_page_SJ(page))  # Преобразовывает текст ответа в словарь Python
    js_objs_SJ.extend(js_obj['objects'])  # Добавляет текущий ответ в js_objs_SJ

count = 0
for i in js_objs_SJ:
    print(print_info(i))
    count += 1
print(count)
