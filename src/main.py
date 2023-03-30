from src.classes import HH, SuperJob
from src.jobs_classes import HHVacancy, SJVacancy, CountMixin
from src.utils import get_top, sorting

# Создание объектов классов HH SuperJob.
# По умолчанию поиск вакансий производится в России, по запросу "Python разработчик developer", без опыта работы.
# При необходимости можно передать экземпляру значения атрибутам "key_text", "area", "experience". Детали в README.
object_HH = HH()
object_SJ = SuperJob()

# Вызов методов классов HH SuperJob, для сбора и записи в общий файл response_data_json вакансий.
object_HH.pass_to_insert_hh()
object_SJ.pass_to_insert_sj()

# Создаются классы Vacancy.
object_HHV = HHVacancy()
object_SJV = SJVacancy()

# Запрос необходимое кол-ва ТОП вакансий по ЗП
top_count = int(input("Введите необходимое кол-во вакансий"))

sorted_array = sorting('response_data.json')
top_to_apply = get_top('response_data.json', top_count)

# Создаются экземпляры классов Vacancy.
# Вызываются необходимые методы классов Vacancy для записи в файл потенциальных вакансий для отклика.
for vacancy in top_to_apply:
    obj_hh = HHVacancy()
    obj_sj = SJVacancy()
    obj_hh.write_to_file()
    obj_sj.write_to_file()

print(CountMixin.get_count_of_vacancy)
print("Вакансии для потенциальных откликов записаны в файл 'best_vacancies.json'. Удачи на интервью!")
