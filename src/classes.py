import json
from abc import ABC, abstractmethod

import requests

from src.connector import Connector


class Engine(ABC):
    """
    Базовый абстрактный класс для классов HH и SuperJob.
    """
    @abstractmethod
    def get_request(self):
        """
        Метод к обязательному переопределению в наследуемых классах.
        """
        pass

    @staticmethod
    def get_connector(file_name='response_data.json'):
        """Статичный метод, возвращающий экземпляр класса Connector """
        connector_object = Connector(file_name)
        return connector_object


class HH(Engine):
    """Класс по работе с API HH."""

    def __init__(self, key_text="Python", area=113, experience="noExperience"):
        """
        Инициализатор класса.
        :param key_text: основной текст поиска вакансий на сайте.
        :param area: страна = по умолчанию Россиия.
        :param experience: ожидаемый опыт кандидата, по умолчанию передается "без опыта".
        """
        self.key_text = key_text  # текст фильтра.
        self.area = area  # Russia - код локации
        self.experience = experience  # код фильтрации опыта работы

    def get_request(self, page=0) -> json:
        """
        Возвращает ответ на запрос https://api.hh.ru/vacancies к API HH,
        для выгрузки всех вакансий, в соответствии с указанными params и инициализированными key_text и area.
        """

        params = {
            'text': self.key_text,
            'area': self.area,
            'page': page,  # индекс страницы, для дальнейшей итерации по страницам
            'per_page': 100,  # max кол-во вакансий на 1 странице
            'experience': self.experience,
            'vacancy_search_order': "salary_desc",  # встроенная сортировка по убыванию ответа по ЗП
        }

        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()

        return data

    def pass_to_insert_hh(self):
        """
        Извлекает кол-во страниц ответа со всеми вакансиями.
        Для каждой страницы вызывает Connect.insert_hh() и дополняет файл в необходимом формате.
        """
        data = json.loads(self.get_request())
        pages = data['pages']  # Узнать кол-во страниц в ответе get_request()
        for page in range(pages):  # записать все страницы в документ, с помощью Connect.insert()
            self.get_connector().insert_hh(json.loads(self.get_request(page)))


class SuperJob(Engine):
    """Класс по работе с API SuperJob."""
    def __init__(self, key_text='Python', area=1, experience=1):
        """
        Инициализатор класса.
        :param key_text: основной текст поиска вакансий на сайте.
        :param area: страна = по умолчанию Россиия.
        :param experience: ожидаемый опыт кандидата, по умолчанию передается "без опыта".
        """
        self.id = "v3.r.137452619.a63bcb7404a9e35b86138b7522ea580731285cad.4636fdc6cb7aa59a9a3960e3a42fd0d53b449a72"
        self.key_text = key_text  # текст фильтра.
        self.area = area  # Russia - код локации
        self.experience = experience  # код фильтрации опыта работы

    def get_request(self) -> dict:
        """
        Метод для запроса к API SuperJob.
        Формирует словарь params на основе init, делает запрос, и заполняет итоговую коллекцию с ответом.
        Для возврата dict с полными данными объкета-ответа перебирается каждая страница ответа page.
        Возвращает data_final с полными максимальными данными (5 страниц по 100 элементов).
        """
        pages = 5  # максимально доступное кол-во на SJ, при максимальном уровне объектов на 1 стр (500 объектов).
        data_final = {'objects': []}

        params = {
            'keywords': self.key_text,
            'page': 0,  # индекс страницы, для дальнейшей итерации по страницам
            'count': 100,  # max кол-во вакансий на 1 странице
            'experience': self.experience,
            'id_country': self.area,
            'order_field': 'payment',  # встроенная сортировка по убыванию ответа по ЗП
            'order_direction': 'desc'
        }
        headers = {"X-Api-App-Id": self.id}

        for i in range(0, pages):
            params['page'] = i
            req = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
            data = req.content.decode()
            req.close()
            python_data = json.loads(data)
            data_final['objects'].extend(python_data['objects'])

        return data_final

    def pass_to_insert_sj(self):
        """
        Отправляет итоговый максимально возможный по кол-ву ответ к обработке и записи в файл в Connector.insert_sj()
        """
        self.get_connector().insert_sj(self.get_request())
