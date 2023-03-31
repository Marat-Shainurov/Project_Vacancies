from src.classes import HH, SuperJob
from src.jobs_classes import CountMixin
from src.utils import get_top, write_to_file_final

# Создание объектов классов HH SuperJob.
# По умолчанию поиск вакансий производится в России, по ключевому слову "Python", без ожидаемого опыта работы.
# При необходимости можно передать экземпляру значения атрибутам "key_text", "area", "experience" - детали в README.
# Для примера, ниже экземплярам обоих классов передан ключевой текст "Python junior"
object_HH = HH(key_text="Python junior")
object_SJ = SuperJob(key_text="Python junior")

# Вызов методов классов HH и SuperJob, для сбора и записи в общий файл response_data_json вакансий.
object_HH.pass_to_insert_hh()
object_SJ.pass_to_insert_sj()

# Запрос необходимого для итоговой записи в vacancies_to_apply.txt кол-ва ТОП вакансий по ЗП.
top_count = int(input("Введите необходимое кол-во вакансий для записи в файл для откликов: "))
top_to_apply = get_top('response_data.json', top_count)

# Создаются экземпляры классов Vacancy, вызывается метод для записи в файл потенциальных вакансий для отклика.
write_to_file_final(top_to_apply, f'../src/vacancies_to_apply.txt')

print(str(CountMixin.get_count_of_vacancy))
print("Вакансии для потенциальных откликов записаны в файл 'best_vacancies.json'. Удачи на интервью!")
