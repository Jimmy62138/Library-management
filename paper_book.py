from book import Book


class PaperBook(Book):
    
    def __init__(self, isbn: int, title: str, author: str) -> None:
        """
        Initializes a PaperBook object with the provided ISBN, title, and author.

        Args:
            isbn (int): The ISBN of the paper book.
            title (str): The title of the paper book.
            author (str): The author of the paper book.
        """
        super().__init__(isbn=isbn, title=title, author=author)
        self.__type = "Papier"
        
    def __str__(self) -> str:
        return self.get_title()
        
    def get_type(self) -> str:
        return self.__type

    def set_type(self, support_type) -> None:
        self.__type = support_type
        