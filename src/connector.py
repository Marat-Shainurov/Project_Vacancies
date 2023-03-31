import json
import os


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате.
    Не забывать проверять целостность данных, что файл с данными не подвергся внешней деградации.
    """

    def __init__(self, data_file):
        """
        Инициализирует экземпляр класса.
        При инициализации, как и при присвоении нового значения data_file,
        проходить проверка на существование и корректность файла.
        """
        path_to_file = f"C:\\Users\\m_sha\\PycharmProjects\\Project_Vacancies\\src\\{data_file}"

        if not os.path.exists(path_to_file):
            f = open(path_to_file, 'w', encoding='utf8')
            f.close()
        else:
            if not os.path.isfile(path_to_file) or path_to_file[-5:] != '.json':
                raise TypeError('Файл потерял актуальность в структуре данных!')

        self.__data_file = data_file

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        """
        Принимает новое значения для файла экземпляра.
        """
        self.__connect(value)
        self.__data_file = value

    def __connect(self, value):
        """
        Проверка на существование файла с данными и создание его при необходимости.
        Также проверить на деградацию и возбудить исключение если файл потерял актуальность в структуре данных.
        """
        path_to_file = f"C:\\Users\\m_sha\\PycharmProjects\\Project_Vacancies\\src\\{value}"

        if not os.path.exists(path_to_file):
            f = open(path_to_file, 'w', encoding='utf8')
            f.close()
        else:
            if not os.path.isfile(path_to_file) or path_to_file[-5:] != '.json':
                raise TypeError('Файл потерял актуальность в структуре данных!')

    def insert_hh(self, data_to_store):
        """
        Запись данных в файл с сохранением структуры и исходных данных.
        Источник - HH.ru
        """

        all_vacancies = data_to_store['items']

        for element in range(len(all_vacancies)):
            data_from_line = {}
            data_from_line['source'] = 'HH'
            data_from_line["id"] = all_vacancies[element]['id']
            data_from_line['name'] = all_vacancies[element]['name']
            data_from_line['salary'] = all_vacancies[element]['salary']
            data_from_line['alternate_url'] = all_vacancies[element]['alternate_url']
            data_from_line['employer'] = all_vacancies[element]['employer']
            data_from_line['snippet'] = all_vacancies[element]['snippet']

            with open(self.__data_file, "a", encoding='utf8') as f:
                json.dump(data_from_line, f, ensure_ascii=False)
                f.write(', ')
                f.write('\n')

    def insert_sj(self, data_to_store):
        """
        Запись данных в файл с сохранением структуры и исходных данных.
        Источник - SuperJob.ru
        """

        all_vacancies = data_to_store['objects']

        for element in range(len(all_vacancies)):
            data_from_line = {}
            data_from_line['source'] = 'SJ'
            data_from_line["id"] = all_vacancies[element]['id']
            data_from_line['name'] = all_vacancies[element]['profession']
            data_from_line['salary'] = {'from': all_vacancies[element]['payment_from'],
                                        'to': all_vacancies[element]['payment_to'],
                                        'currency': all_vacancies[element]['currency']}
            data_from_line['alternate_url'] = all_vacancies[element]['link']
            data_from_line['employer'] = all_vacancies[element]['firm_name']
            data_from_line['snippet'] = all_vacancies[element]['work']

            with open(self.__data_file, "a", encoding='utf8') as f:
                json.dump(data_from_line, f, ensure_ascii=False)
                f.write(', ')
                f.write('\n')

    def select(self, query: dict):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """

        res = []

        with open(self.__data_file, encoding='utf8') as f:
            content = f.read()
            content_new = f"[{content.strip().strip(',')}]"

        data = json.loads(content_new)
        query_key = list(query.keys())[0]

        for element in data:
            if not element[query_key]:
                return
            if element[query_key] == query[query_key]:
                res.append(element)

        return res


    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """
        pass
