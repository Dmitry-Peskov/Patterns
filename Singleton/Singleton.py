class Database:
    __database_connection = None
    __data: str = ''

    def __new__(cls):
        if cls.__database_connection is None:
            cls.__database_connection: Database = object.__new__(cls)
            print('Установлено соединение с БД')
        return cls.__database_connection

    def select(self) -> str:
        return self.__data

    def insert(self, data: str):
        self.__data = data


if __name__ == "__main__":
    connect_1 = Database()
    connect_1.insert('Добавлено в 1 подключении')

    connect_2 = Database()
    print('Результат запроса во 2 подключении: ', connect_2.select())

    print(f"connect_1 ссылается на {connect_1}; connect_2 ссылается на {connect_2}")
