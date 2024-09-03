import sqlite3

from digital_book import LivreNumerique
from paper_book import LivrePapier
from users import Utilisateur


def singleton(cls):
    _instance = {}
    
    def get_instance(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return get_instance


@singleton
class Bibliotheque:
    
    def __init__(self) -> None:
        self.__create_tables()

    @staticmethod
    def __execute_query(query) -> list:
        conn = sqlite3.connect("database/database.db")
        c = conn.cursor()
        c.execute(query)
        res = c.fetchall()
        conn.commit()
        conn.close()
        return res

    def __create_tables(self):
        self.__execute_query("""
        CREATE TABLE IF NOT EXISTS Books (
        Isbn INTEGER PRIMARY KEY UNIQUE NOT NULL,
        Title VARCHAR (60) NOT NULL,
        Autor VARCHAR (30) NOT NULL,
        Type VARCHAR (10) NOT NULL,
        Lend INTEGER DEFAULT 0,
        UserId INT REFERENCES Users (UserID) DEFAULT NULL
        ); 
        """)
        self.__execute_query("""
        CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR (30) UNIQUE NOT NULL
        ); 
        """)
        
    def add_book(self, book):
        self.__execute_query(f"INSERT INTO Books (Isbn, Title, Autor, Type) VALUES ({book.get_isbn()}, '{book.get_title()}', '{book.get_autor()}', '{book.get_type()}');")
        
    def delete_book(self, isbn):
        self.__execute_query(f"DELETE FROM Books WHERE Isbn = {isbn};")
   
    def update_book(self, book):
        self.__execute_query(f"""
        UPDATE Books
        SET
        Title = '{book.get_title()}',
        Autor = '{book.get_autor()}',
        Type = '{book.get_type()}'
        WHERE Isbn = {book.get_isbn()};
        """)

    def borrow_book(self, book, user):
        uid = self.__execute_query(f"SELECT UserID FROM Users WHERE Name = '{user.get_name()}';")[0][0]
        self.__execute_query(f"""
        UPDATE Books
        SET
        Lend = Lend + 1,
        UserId = {uid}
        WHERE Isbn = {book.get_isbn()};
        """)
        
    def return_book(self, book):
        self.__execute_query(f"""
        UPDATE Books
        SET
        UserId = NULL
        WHERE Isbn = {book.get_isbn()};
        """)

    def get_all_books(self) -> list:
        return [
            LivrePapier(book[0], book[1], book[2]) if book[3] == "papier"
            else LivreNumerique(book[0], book[1], book[2])
            for book in self.__execute_query("SELECT * FROM Books")
        ]

    def get_available_books(self) -> list:
        return [
            LivrePapier(book[0], book[1], book[2]) if book[3] == "papier"
            else LivreNumerique(book[0], book[1], book[2])
            for book in self.__execute_query("SELECT * FROM Books WHERE UserId IS NULL")
        ]

    def get_unavailable_books(self) -> list:
        return [
            LivrePapier(book[0], book[1], book[2]) if book[3] == "papier"
            else LivreNumerique(book[0], book[1], book[2])
            for book in self.__execute_query("SELECT * FROM Books WHERE UserId IS NOT NULL")
        ]

    def get_users(self) -> [Utilisateur]:
        return [Utilisateur(user[1]) for user in self.__execute_query("SELECT * FROM Users;")]


if __name__ == "__main__":
    library = Bibliotheque()
    print(library.get_all_books())
    