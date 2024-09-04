from book import Book


class PaperBook(Book):
    
    def __init__(self, isbn: int, title: str, autor: str) -> None:
        super().__init__(isbn=isbn, title=title, autor=autor)
        self.__type = "papier"
        
    def __str__(self) -> str:
        return self.get_title()
        
    def get_type(self) -> str:
        return self.__type
        