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
        self.vacancy_salary = self.vacancy['salary']
        self.employer = self.vacancy['employer']
        self.source = self.vacancy['source']

    def __gt__(self, other) -> bool:
        """
        Сравнивает 2 вакансии классов Vacancy, HHVacancy, SJVacancy по ЗП. Возвращает bool.
        """
        return self.vacancy['salary'] > other.vacancy['salary']

    def __lt__(self, other) -> bool:
        """
        Сравнивает 2 вакансии классов Vacancy, HHVacancy, SJVacancy по ЗП. Возвращает bool.
        """
        return self.vacancy['salary'] < other.vacancy['salary']

    def __str__(self):
        return f'{self.source}: {self.employer}, зарплата: {self.vacancy_salary} руб/мес, компания: {self.employer}, ссылка: {self.vacancy_url}'

    def __repr__(self):
        return f"{self.__class__.__name__}({self.vacancy})"

    def write_to_file(self, path_to_file):
        with open(path_to_file, "a", encoding='utf8') as f:
            f.write("\n")
            f.write("Вакансия: ")
            f.write("\n")
            f.write(self.__str__())


class CountMixin:
    """Класс Mixin для подсчета вакансий ресурсов HH и SJ."""

    # Счетчики выданных вакансий
    count_HH = 0
    count_SJ = 0

    def __init__(self):
        CountMixin.count_SJ += 1
        CountMixin.count_HH += 1

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
