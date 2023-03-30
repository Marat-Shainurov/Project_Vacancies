class Vacancy:
    __slots__ = ("vacancy_name", "vacancy_url", "vacancy_description", "vacancy_salary")

    def __init__(self):
        super().__init__()
        self.vacancy_name = None
        self.vacancy_url = None
        self.vacancy_description = None
        self.vacancy_salary = None

    def __str__(self):
        pass

    def __repr__(self):
        pass


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


class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    """ HeadHunter Vacancy """

    def __str__(self):
        return f'HH: {self.company_name}, зарплата: {self.salary} руб/мес'



class SJVacancy(Vacancy, CountMixin):  # add counter mixin
    """ SuperJob Vacancy """

    def __str__(self):
        return f'SJ: {self.company_name}, зарплата: {self.salary} руб/мес'