class Vacancy:
    """Базовый класс для HHVacancy и SJVacancy"""
    __slots__ = (
    "vacancy_name", "vacancy_url", "vacancy_description", "vacancy_salary", "vacancy", "employer", "source")

    def __init__(self, vacancy):
        """
        Инициализирует все атрибуты на основе отсортированного элемента функциями sorting() и get_top()
        """
        super().__init__()
        self.vacancy: dict = vacancy
        self.vacancy_name = self.vacancy['name']
        self.vacancy_url = self.vacancy['alternate_url']
        self.vacancy_description = self.vacancy['snippet']
        self.vacancy_salary = self.vacancy['salary_to_be_sorted_by']
        self.employer = self.vacancy['employer']
        self.source = self.vacancy['source']

    def __gt__(self, other) -> bool:
        """
        Сравнивает 2 вакансии классов Vacancy, HHVacancy, SJVacancy по ЗП. Возвращает bool.
        """
        return self.vacancy_salary > other.vacancy_salary

    def __lt__(self, other) -> bool:
        """
        Сравнивает 2 вакансии классов Vacancy, HHVacancy, SJVacancy по ЗП. Возвращает bool.
        """
        return self.vacancy_salary < other.vacancy_salary

    def __str__(self):
        return f'{self.source}, {self.vacancy_name}, зарплата: {self.vacancy_salary} руб/мес, ' \
               f'Компания: {self.employer}, \nссылка для отклика: {self.vacancy_url}\n'

    def __repr__(self):
        return f"{self.__class__.__name__}({self.vacancy})"

    def write_to_file(self, path_to_file):
        with open(path_to_file, "a", encoding='utf8') as f:
            f.write("\n")
            f.write("Вакансия: ")
            f.write(self.__str__())


class CountMixin:
    """Класс Mixin для подсчета инициализированных вакансий ресурсов HH и SJ."""

    # Счетчики собранных вакансий
    count_HH = 0
    count_SJ = 0
    count_V = 0

    def __init__(self):
        if self.__class__.__name__ == 'HHVacancy':
            CountMixin.count_HH += 1
        elif self.__class__.__name__ == 'SJVacancy':
            CountMixin.count_SJ += 1
        else:
            CountMixin.count_V += 1

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        return f"Вакансий HH - {CountMixin.count_HH}, Вакансий SJ - {CountMixin.count_SJ}."


class HHVacancy(Vacancy, CountMixin):
    """ HeadHunter Vacancy """
    pass


class SJVacancy(Vacancy, CountMixin):
    """ SuperJob Vacancy """
    pass

object_1 = HHVacancy({
        'source': 'HH', 'id': '73595241', 'name': 'Специалист службы поддержки с техническими знаниями (TOOLS)',
        'salary': {'from': 15000, 'to': 39000, 'currency': 'RUR', 'gross': False},
        'alternate_url': 'https://hh.ru/vacancy/73595241',
        'employer': {'id': '9498112', 'name': 'Яндекс Крауд', 'url': 'https://api.hh.ru/employers/9498112',
                     'alternate_url': 'https://hh.ru/employer/9498112', 'logo_urls': None,
                     'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9498112', 'trusted': True},
        'snippet': {
            'requirement': 'Умеете читать языки JavaScript, HTML и <highlighttext>Python</highlighttext>. Имеете высшее или неоконченное высшее образование (техническое будет плюсом). Помогали людям онлайн. ',
            'responsibility': 'Отвечать на сообщения пользователей по почте и в чатах. Консультировать их о вопросах, связанных с Яндексом. Передавать информацию разработчикам и...'},
        'salary_to_be_sorted_by': 15000
    })


print(str(object_1))