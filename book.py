from unicodedata import normalize


def normalizer(text: str) -> str:
    """
    function to remove special characters
    Args:
        text (str): string to process

    Returns:
        string without special characters
    """
    normalized_text = normalize('NFD', text)
    normalized_text = normalized_text.encode('ascii', 'ignore').decode("utf-8")
    return normalized_text


class Book:
    def __init__(self, isbn: int, title: str, autor: str) -> None:
        self.__isbn: int = isbn
        self.__title: str = (normalizer(title)).capitalize()
        self.__autor: str = autor.title()
        
    def __str__(self) -> str:
        return self.__title

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title) -> None:
        self.__title = (normalizer(title)).capitalize()
        
    def get_autor(self) -> str:
        return self.__autor
    
    def set_autor(self, autor) -> None:
        self.__autor = autor.title()
        
    def get_isbn(self) -> int:
        return self.__isbn
        
        
if __name__ == "__main__":
    
    livre = Book(1456789, "il était une fois !", "stephen king", )
    print(livre.get_title())
    