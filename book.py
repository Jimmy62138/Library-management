from unicodedata import normalize

class Livre:
    def __init__(self, isbn: int, title: str, autor: str) -> None:
        self.__isbn: int = isbn
        self.__title: str = (self.normalizer(title)).capitalize()
        self.__autor: str = autor.title()
        
    def __str__(self) -> str:
        return self.__title
        
    def normalizer(self, text: str) -> str:
        normalized_text = normalize('NFD', text)
        normalized_text = normalized_text.encode('ascii', 'ignore').decode("utf-8")
        return normalized_text
    
    def get_title(self) -> str:
        return self.__title

    def set_title(self, title) -> None:
        self.__title = title
        
    def get_autor(self) -> str:
        return self.__autor
    
    def set_autor(self, autor) -> None:
        self.__autor = autor
        
    def get_isbn(self) -> int:
        return self.__isbn
        
        
if __name__ == "__main__":
    
    livre = Livre(1456789, "il était une fois !", "stephen king", )
    print(livre.get_title())
    