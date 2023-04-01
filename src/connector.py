import json
import os


class Connector:
    """
    Класс коннектор к json файлу.
    Проверяет целостность данных, что файл с данными не подвергся внешней деградации.
    """

    def __init__(self, data_file):
        """
        Инициализирует экземпляр класса.
        При инициализации, как и при присвоении нового значения data_file,
        проходить проверка на существование и корректность файла, создание нового файла при необходимости.
        """
        self.path_to_file = f"../src/{data_file}"

        if not os.path.exists(self.path_to_file):
            f = open(self.path_to_file, 'w', encoding='utf8')
            f.close()
        else:
            if not os.path.isfile(self.path_to_file) or self.path_to_file[-5:] != '.json':
                raise TypeError('Файл потерял актуальность в структуре данных!')

        self.__data_file = data_file

    @property
    def data_file(self):
        """Getter для data_file"""
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        """
        Принимает новое значения для файла экземпляра, проводя через проверку в __connect().
        """
        self.__connect(value)
        self.__data_file = value

    def __connect(self, value):
        """
        Проверка на существование файла с данными и создание его при необходимости.
        Также проверить на деградацию и возбудить исключение если файл потерял актуальность в структуре данных.
        """
        self.path_to_file = f"../src/{value}"

        if not os.path.exists(self.path_to_file):
            f = open(self.path_to_file, 'w', encoding='utf8')
            f.close()
        else:
            if not os.path.isfile(self.path_to_file) or self.path_to_file[-5:] != '.json':
                raise TypeError('Файл потерял актуальность в структуре данных!')

    def insert_hh(self, data_to_store):
        """
        Запись данных в файл в едином формате с сохранением структуры и исходных данных.
        Источник - ответ запроса к API HH.
        """

        all_vacancies = data_to_store['items']

        for element in range(len(all_vacancies)):
            data_from_line = {}
            data_from_line['source'] = 'HH'
            data_from_line["id"] = all_vacancies[element]['id']
            data_from_line['name'] = all_vacancies[element]['name']
            data_from_line['salary'] = all_vacancies[element]['salary']
            data_from_line['alternate_url'] = all_vacancies[element]['alternate_url']
            data_from_line['employer'] = all_vacancies[element]['employer']['name']
            data_from_line['snippet'] = all_vacancies[element]['snippet']

            with open(self.__data_file, "a", encoding='utf8') as f:
                json.dump(data_from_line, f, ensure_ascii=False)
                f.write(', ')
                f.write('\n')

    def insert_sj(self, data_to_store):
        """
        Запись данных в файл в едином формате с сохранением структуры и исходных данных.
        Источник - ответ запроса к API SuperJob.ru.
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

        with open(self.path_to_file, encoding='utf8') as f:
            content = f.read()
            content_new = f"[{content.strip().strip(',')}]"

        data = json.loads(content_new)
        query_key = list(query.keys())[0]

        for element in data:
            try:
                if element[query_key] == query[query_key]:
                    res.append(element)
            except KeyError:
                pass

        if not res:
            return None
        else:
            return res


    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запросу,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """

        res = []
        with open(self.path_to_file, encoding='utf8') as f:
            content = f.read()
            content_new = f"[{content.strip().strip(',')}]"
        data = json.loads(content_new)
        query_key = list(query.keys())[0]

        for element in data:
            try:
                if element[query_key] != query[query_key]:
                    res.append(element)
            except KeyError:
                res.append(element)

        if len(res) != len(data):
            with open(self.path_to_file, "w") as f:
                f.write('')
            for el in res:
                with open(self.path_to_file, "a", encoding='utf8') as f:
                    json.dump(el, f, ensure_ascii=False)
                    f.write(', ')
                    f.write('\n')
