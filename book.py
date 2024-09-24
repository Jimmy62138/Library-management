from unicodedata import normalize


def normalizer(text: str) -> str:
    """
    function to remove special characters
    Args:
        text (str): string to process

    Returns:
        string without special characters
    """
    text = text.replace("'", " ")
    normalized_text = normalize('NFD', text)
    normalized_text = normalized_text.encode('ascii', 'ignore').decode("utf-8")
    return normalized_text


class Book:
    def __init__(self, isbn: int, title: str, author: str) -> None:
        """
        A class representing a book with attributes for ISBN, title, and author.
        Methods to get and set the title, author, and ISBN of the book.

        Attributes:
            isbn (int): The ISBN of the book.
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.__isbn: int = isbn
        self.__title: str = normalizer(title).capitalize()
        self.__author: str = author.title()
        
    def __str__(self) -> str:
        return self.__title

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title) -> None:
        self.__title = normalizer(title).capitalize()
        
    def get_author(self) -> str:
        return self.__author
    
    def set_author(self, author) -> None:
        self.__author = author.title()

    def set_isbn(self, isbn: int) -> None:
        self.__isbn = isbn

    def get_isbn(self) -> int:
        return self.__isbn
        
        
if __name__ == "__main__":
    
    livre = Book(1456789, "il était une fois !", "stephen king", )
    print(livre.get_title())
    