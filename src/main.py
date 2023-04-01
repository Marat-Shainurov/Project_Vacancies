from src.jobs_classes import CountMixin
from src.utils import get_top, write_to_file_final, get_started
import time

# Интерактив с пользователем, создание объектов классов HH SuperJob.
objects = get_started()

# Вызов методов классов HH и SuperJob, для сбора вакансий и записи в общий файл response_data_json.
objects[0].pass_to_insert_hh()
objects[1].pass_to_insert_sj()

# Запрос необходимого кол-ва ТОП вакансий по ЗП, для итоговой записи в vacancies_to_apply.txt.
top_count = int(input("Введите необходимое кол-во вакансий для записи в файл для откликов: "))
top_to_apply = get_top('response_data.json', top_count)

# Создаются экземпляры классов Vacancy, вызывается метод для записи в файл потенциальных вакансий для отклика.
write_to_file_final(top_to_apply, f'../src/vacancies_to_apply.txt')

# Завершение программы
print()
print("Вакансии для потенциальных откликов записаны в файл 'vacancies_to_apply.txt'.")
print(CountMixin().get_count_of_vacancy)
print("Удачи на интервью! :)")
