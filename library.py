import sqlite3

from digital_book import DigitalBook
from paper_book import PaperBook
from users import Users


def singleton(cls):
    """
    function that allows you to have only one instance of a class
    Args:
        cls: class to instantiate

    Returns:
        instantiate class
    """
    _instance = {}
    
    def get_instance(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return get_instance


@singleton
class Library:
    
    def __init__(self) -> None:
        self.__create_tables()

    @staticmethod
    def __execute_query(query) -> list:
        """
        static method to execute an SQL query
        Args:
            query: SQL query

        Returns:
            SQL result
        """
        conn = sqlite3.connect("database/database.db")
        c = conn.cursor()
        c.execute(query)
        res = c.fetchall()
        conn.commit()
        conn.close()
        return res

    def __create_tables(self) -> None:
        """
        Automatically create needed SQL tables if not exists
        """
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
        
    def add_book(self, book: DigitalBook | PaperBook):
        """
        Insert a book into database
        Args:
            book (DigitalBook | PaperBook): book
        """
        self.__execute_query(f"""INSERT INTO Books (Isbn, Title, Autor, Type) VALUES (
                                {book.get_isbn()}, '{book.get_title()}', '{book.get_autor()}', '{book.get_type()}');
                                """)
        
    def delete_book(self, isbn: int):
        """
        Delete a book by ISBN
        Args:
            isbn (int): ISBN number
        """
        self.__execute_query(f"DELETE FROM Books WHERE Isbn = {isbn};")
   
    def update_book(self, book: DigitalBook | PaperBook):
        self.__execute_query(f"""
        UPDATE Books
        SET
        Title = '{book.get_title()}',
        Autor = '{book.get_autor()}',
        Type = '{book.get_type()}'
        WHERE Isbn = {book.get_isbn()};
        """)

    def borrow_book(self, book: DigitalBook | PaperBook, user: Users):
        """
        associates a user with a book in a database
        Args:
            book(DigitalBook | PaperBook): a book borrowed
            user(Users): book borrower
        """
        uid = self.__execute_query(f"SELECT UserID FROM Users WHERE Name = '{user.get_name()}';")[0][0]
        self.__execute_query(f"""
        UPDATE Books
        SET
        Lend = Lend + 1,
        UserId = {uid}
        WHERE Isbn = {book.get_isbn()};
        """)
        
    def return_book(self, book: DigitalBook | PaperBook):
        """
        Return a book by setting the null value of UserId to database
        Args:
            book(LivreNumérique | LivrePapier): book to return

        """
        self.__execute_query(f"""
        UPDATE Books
        SET
        UserId = NULL
        WHERE Isbn = {book.get_isbn()};
        """)

    def get_all_books(self) -> [PaperBook | DigitalBook]:
        """
            Function to get all books from database
        Returns:
            An array with all books from database
        """
        return [
            PaperBook(book[0], book[1], book[2]) if book[3] == "papier"
            else DigitalBook(book[0], book[1], book[2])
            for book in self.__execute_query("SELECT * FROM Books")
        ]

    def get_available_books(self) -> [PaperBook | DigitalBook]:
        """
        return the list of all unloaned books
        Returns:
            Array with all unloaned books
        """
        return [
            PaperBook(book[0], book[1], book[2]) if book[3] == "papier"
            else DigitalBook(book[0], book[1], book[2])
            for book in self.__execute_query("SELECT * FROM Books WHERE UserId IS NULL")
        ]

    def get_unavailable_books(self) -> [PaperBook | DigitalBook]:
        """
        return the list of all loaned books
        Returns:
            Array with all loaned books
        """
        return [
            PaperBook(book[0], book[1], book[2]) if book[3] == "papier"
            else DigitalBook(book[0], book[1], book[2])
            for book in self.__execute_query("SELECT * FROM Books WHERE UserId IS NOT NULL")
        ]

    def get_users(self) -> [Users]:
        """
            Gett all users
        Returns:
            An array with all users from Users table
        """
        return [Users(user[1]) for user in self.__execute_query("SELECT * FROM Users;")]

    def get_statistics(self) -> []:
        """
        Returns: All books with their associate number of lend from books table

        """
        return self.__execute_query("SELECT Title, Lend FROM Books ORDER BY Lend DESC")


if __name__ == "__main__":
    library = Library()
    print(library.get_all_books())
    