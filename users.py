"""A class representing a user with methods to add, get, and delete users from the database."""

import sqlite3


class Users:

    DB = "database/database.db"
    """DB (str): The path to the database file."""

    def __init__(self, nom: str) -> None:
        """
        Initializes a Users object with the provided name.

        Args:
            nom (str): The name of the user.
        """
        self.__name: str = nom.capitalize()

    def __execute_query(self, query):
        """
        Executes an SQL query.

        Args:
            query: SQL query

        Returns:
            SQL result
        """
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
        """
        Adds the user to the database.

        Returns:
            None
        """
        self.__execute_query(f"INSERT INTO Users (Name) VALUES ('{self.__name}');")

    def get_user(self) -> []:
        """
        Retrieves the user from the database.

        Returns:
            list: The user from the database
        """
        return self.__execute_query(f"SELECT Name FROM Users WHERE Name = '{self.__name}'")

    def delete_user(self) -> None:
        """
        Deletes the user from the database.

        Returns:
            None
        """
        self.__execute_query(f"DELETE FROM Users WHERE Name = '{self.__name}';")


if __name__ == "__main__":

    user = Users("user_test")
    user.get_user()
    # user.add_user()
