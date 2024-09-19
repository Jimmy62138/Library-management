import sqlite3


class Users:
    DB = "database/database.db"
    def __init__(self, nom: str) -> None:
        self.__name: str = nom.capitalize()

    def __execute_query(self, query):
        conn = sqlite3.connect(self.DB)
        c = conn.cursor()
        c.execute(query)
        res = c.fetchall()
        conn.commit()
        conn.close()
        return res

    def __str__(self) -> str:
        return self.__name

    def get_name(self):
        return self.__name

    def add_user(self) -> None:
        self.__execute_query(f"INSERT INTO Users (Name) VALUES ('{self.__name}');")

    def get_user(self) -> []:
        return self.__execute_query(f"SELECT Name FROM Users WHERE Name = '{self.__name}'")

    def delete_user(self) -> None:
        self.__execute_query(f"DELETE FROM Users WHERE Name = '{self.__name}';")


if __name__ == "__main__":

    user = Users("user_test")
    user.get_user()
    # user.add_user()
