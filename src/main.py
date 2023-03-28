# Задача: нужно написать парсер для сайта, который собирает текущие вакансии в России для Python-разработчиков,
# а также составить документ для возможных откликов.

from src.classes import Engine, HH, SuperJob
from src.connector import Connector

obj_HH = HH()
obj_HH.save_data_to_file()
