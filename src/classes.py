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
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        connector_object = Connector(file_name)
        return connector_object


class HH(Engine):
    """Класс по работе с API HH."""

    def __init__(self):
        self.key_text = 'Python'
        self.area = 1


    def get_request(self, page=0):
        """Возвращает ответ на запрос к API HH."""

        params = {
            'text': self.key_text,  # текст фильтра, в имени должно быть Python, доп данные через запятую.
            'area': self.area,  # код локации (1 - Мск)
            'page': page,  # индекс страницы
            'per_page': 100  # кол-во вакансий на 1 странице
        }

        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()

        return data

    def save_data_to_file(self):
        """Сохраняет первичный ответ на запрос к API HH в файл HH_data.json."""
        data_to_store = []
        for page in range(0, 10):
            data = self.get_request(page)
            data_to_store.append(data)
        with open('HH_data.json', "w", encoding='utf8') as f:
            json.dump(data_to_store, f, indent=2, ensure_ascii=False)


class SuperJob(Engine):
    def get_request(self):
        pass