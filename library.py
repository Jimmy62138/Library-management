import sqlite3

def singleton(cls):
    _instance = {}
    
    def get_instance(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return get_instance
   
   
@singleton
class Bibliotheque():
    
    def __init__(self) -> None:
        self.__create_tables()
            
    def __execute_query(self, query):
        conn = sqlite3.connect("database/database.db")
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        conn.close()
        
    def __create_tables(self):
        self.__execute_query("""
        CREATE TABLE IF NOT EXISTS Books (
        Isbn INTEGER PRIMARY KEY UNIQUE NOT NULL,
        Title VARCHAR (60) NOT NULL,
        Autor VARCHAR (30) NOT NULL,
        Type VARCHAR (10) NOT NULL,
        UserId INT REFERENCES Users (UserID) DEFAULT NULL
        ); 
        """)
        self.__execute_query("""
        CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR (30) NOT NULL
        ); 
        """)
        
    def add_book(self, book):
        self.__execute_query(f"INSERT INTO Books (Isbn, Title, Autor, Type) VALUES ({book.get_isbn()}, '{book.get_title()}', '{book.get_autor()}', '{book.get_type()}');")
        
    def delete_book(self, book):
        self.__execute_query(f"DELETE FROM Books WHERE Isbn = {book.get_isbn()};")
   
    def update_book(self, book):
        self.__execute_query(f"""
        UPDATE Books
        SET
        Title = '{book.get_title()}',
        Autor = '{book.get_autor()}',
        Type = '{book.get_type()}'
        WHERE Isbn = {book.get_isbn()};
        """)

           
if __name__ == "__main__":
    
    # test singleton
    library = Bibliotheque()

    
    