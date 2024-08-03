import sqlite3

class Utilisateur():
    def __init__(self, nom: str) -> None:
        self.__name: str = nom.capitalize()
        
    def __execute_query(self, query):
        conn = sqlite3.connect("database/database.db")
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        conn.close()
        
    def __str__(self) -> str:
        return self.__name  
    
    def get_user(self):
        return self.__name
        
    def add_user(self) -> None:
        self.__execute_query(f"INSERT INTO Users (Name) VALUES ('{self.__name}');")
        
    def delete_user(self) -> None:
        self.__execute_query(f"DELETE FROM Users WHERE Name = '{self.__name}';")
        
        
if __name__ == "__main__":
    jimmy = Utilisateur("Boris")
    
    jimmy.delete_user()
