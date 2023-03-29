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
        path_to_file = f"../src/{data_file}"

        if not os.path.exists(path_to_file):
            f = open(path_to_file, 'w', encoding='utf8')
            f.close()
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
        path_to_file = f"../src/{value}"

        if not os.path.exists(path_to_file):
            f = open(value, 'w', encoding='utf8')
            f.close()
        if not os.path.isfile(path_to_file) or path_to_file[-5:] != '.json':
            raise TypeError('Файл потерял актуальность в структуре данных!')

    def insert(self, data_to_store):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """

        all_vacancies = data_to_store['items']

        for element in range(len(all_vacancies)):
            data_from_line = {}
            data_from_line["id"] = all_vacancies[element]['id']
            # # data_to_store[element].get('id', {}).get('id', None)
            data_from_line['name'] = all_vacancies[element]['name']
            data_from_line['salary'] = all_vacancies[element]['salary']
            data_from_line['alternate_url'] = all_vacancies[element]['alternate_url']
            data_from_line['employer'] = all_vacancies[element]['employer']
            data_from_line['snippet'] = all_vacancies[element]['snippet']

            with open(self.__data_file, "a", encoding='utf8') as f:
                json.dump(data_from_line, f, ensure_ascii=False)
                f.write(', ')
                f.write('\n')

    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        pass

    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """
        pass


if __name__ == '__main__':
    df = Connector('df.json')

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert(data_for_file)
    data_from_file = df.select(dict())
    assert data_from_file == [data_for_file]

    df.delete({'id': 1})
    data_from_file = df.select(dict())
    assert data_from_file == []
