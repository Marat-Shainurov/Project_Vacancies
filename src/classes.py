# 1. Опишите логику записи найденных вакансий в один json файл.
# 2. Опишите логику вывода информации по данным пользователя.
# Пользователь может вывести 10 самых высокооплачиваемых вакансий из файла с результатами или вакансии,
# в которых не требуется опыт работы.

from abc import ABC, abstractmethod
from src.connector import Connector
import requests
import json


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name='response_data.json'):
        """ Возвращает экземпляр класса Connector """
        connector_object = Connector(file_name)
        return connector_object


class HH(Engine):
    """Класс по работе с API HH."""

    def __init__(self, key_text='Python разработчик developer', area=113, experience="noExperience"):
        self.key_text = key_text  # текст фильтра.
        self.area = area  # Russia - код локации
        self.experience = experience

    def get_request(self, page=0) -> json:
        """
        Возвращает ответ на запрос https://api.hh.ru/vacancies к API HH,
        для выгрузки всех вакансий, в соответствии с указанными params и инициализированными key_text и area.
        """

        params = {
            'text': self.key_text,  # текст фильтра.
            'area': self.area,  # код локации
            'page': page,  # индекс страницы
            'per_page': 100,  # кол-во вакансий на 1 странице
            'experience': self.experience,
            'vacancy_search_order': 'salary_desc'
        }

        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()

        return data

    def pass_to_insert_hh(self):
        """
        Извлекает кол-во страниц ответа со всеми вакансиями.
        Для каждой страницы вызывает Connect.insert() и дополняет файл в необходимом формате.
        """
        data = json.loads(self.get_request())
        pages = data['pages']  # Узнать кол-во страниц в ответе get_request()
        for page in range(pages):  # записать все страницы в документ, с помощью Connect.insert()
            self.get_connector().insert_hh(json.loads(self.get_request(page)))


class SuperJob(Engine):

    def __init__(self, key_text='Python разработчик developer', experience=1):
        self.id = "v3.r.137452619.a63bcb7404a9e35b86138b7522ea580731285cad.4636fdc6cb7aa59a9a3960e3a42fd0d53b449a72"
        self.key_text = key_text
        self.experience = experience

    def get_request(self) -> json:
        pages = 5  # максимально доступное кол-во на SJ, при максимальном уровне объектов на 1 стр (500 объектов).
        data_final = {'objects': []}

        params = {
            'keywords': self.key_text,
            'page': 0,
            'count': 100,
            'experience': self.experience,
            'id_country': 1,
            'order_field': 'payment',
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
        Отправляет итоговый максимально возможный по кол-ву ответ к обработке и записи в файл в Connector.insert()
        """
        self.get_connector().insert_sj(self.get_request())
