class Vacancy:
    __slots__ = ("vacancy_name", "vacancy_url", "vacancy_description", "vacancy_salary")

    def __init__(self):
        self.vacancy_name = None
        self.vacancy_url = None
        self.vacancy_description = None
        self.vacancy_salary = None

    def __str__(self):
        pass

    def __repr__(self):
        pass


class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        pass

class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    def __str__(self):
        return f'HH: {self.company_name}, зарплата: {self.salary} руб/мес'



class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __str__(self):
        return f'SJ: {self.company_name}, зарплата: {self.salary} руб/мес'