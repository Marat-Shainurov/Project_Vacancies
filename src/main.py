from src.classes import HH, SuperJob
from src.jobs_classes import CountMixin
from src.utils import get_top, write_to_file_final

# Создание объектов классов HH SuperJob.
# По умолчанию поиск вакансий производится в России, по запросу "Python", без опыта работы.
# При необходимости можно передать экземпляру значения атрибутам "key_text", "area", "experience" - детали в README.
object_HH = HH()
object_SJ = SuperJob()

# Вызов методов классов HH SuperJob, для сбора и записи в общий файл response_data_json вакансий.
object_HH.pass_to_insert_hh()
object_SJ.pass_to_insert_sj()

# Запрос необходимое кол-ва ТОП вакансий по ЗП
top_count = int(input("Введите необходимое кол-во вакансий: "))
top_to_apply = get_top('response_data.json', top_count)

# Создаются экземпляры классов Vacancy.
# Вызываются необходимые методы классов Vacancy для записи в файл потенциальных вакансий для отклика.
write_to_file_final(top_to_apply, f'../src/vacancies_to_apply.txt')

print(CountMixin.get_count_of_vacancy)
print("Вакансии для потенциальных откликов записаны в файл 'best_vacancies.json'. Удачи на интервью!")
