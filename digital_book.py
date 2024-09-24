from book import Book


class DigitalBook(Book):
    __type = "Numérique"

    def __init__(self, isbn: int, title: str, author: str) -> None:
        """
        A class representing a digital book that inherits from the Book class.

        Attributes:
            self.__type (str): The type of the digital book.

        Methods:
            __str__: Returns the title of the digital book.
            get_type: Returns the type of the digital book.
        """
        super().__init__(isbn=isbn, title=title, author=author)
        
    def __str__(self) -> str:
        return self.get_title()
        
    def get_type(self) -> str:
        return self.__type

    def set_type(self, support_type) -> None:
        self.__type = support_type
        