'''
Livre () Mother encapsulé
params:
			private titre :
			private auteur:
			private isbn

		method:
			Mettre à jour les informations du livre : Titre Auteur
''';
from unicodedata import normalize

class Livre:
    def __init__(self, title: str, autor: str, isbn: int) -> None:
        self.__title: str = (self.normalizer(title)).capitalize()
        self.__autor: str = autor.lower()
        self.__isbn: int = isbn
        
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
    
    livre = Livre("il était une fois !", "stephen king", 1456789)
    print(livre.get_title())