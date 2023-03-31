import pytest
from src.classes import Engine, HH, SuperJob
from src.connector import Connector
from src.jobs_classes import Vacancy, HHVacancy, SJVacancy


@pytest.fixture
def testing_instance_hh():
    obj = HH(key_text="Python", area=113, experience="noExperience")
    return obj


@pytest.fixture
def testing_instance_connector():
    obj = Connector('response_data.json')
    return obj


@pytest.fixture
def testing_instance_sj():
    obj = SuperJob(key_text='Python', area=1, experience=1)
    return obj


@pytest.fixture
def testing_instance_connector_example():
    obj = Connector('../tests/test_response_data.json')
    return obj


@pytest.fixture
def testing_instance_Vacancy():
    data = {
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
    }
    obj = Vacancy(data)
    return obj


@pytest.fixture
def testing_instance_HHVacancy():
    data = {
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
    }
    obj = HHVacancy(data)
    return obj


@pytest.fixture
def testing_instance_SJVacancy():
    data = {
        'source': 'SJ', 'id': 45454614, 'name': 'Специалист службы поддержки с техническими знаниями',
        'salary': {'from': 15000, 'to': 39000, 'currency': 'rub'},
        'alternate_url': 'https://makhachkala.superjob.ru/vakansii/specialist-sluzhby-podderzhki-s-'
                         'tehnicheskimi-znaniyami-45454614.html',
        'employer': 'Яндекс',
        'snippet': None,
        'salary_to_be_sorted_by': 15000}
    obj = SJVacancy(data)
    return obj
