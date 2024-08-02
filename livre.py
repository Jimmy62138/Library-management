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
        self.__title = (self.normalizer(title)).capitalize()
        self.__autor = autor.lower()
        self.__isbn = isbn
        
    def normalizer(self, text: str) -> str:
        normalized_text = normalize('NFD', text)
        normalized_text = normalized_text.encode('ascii', 'ignore').decode("utf-8")
        return normalized_text
    
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title
        
    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor
        
    def get_isbn(self):
        return self.__isbn
        
        
if __name__ == "__main__":
    
    livre = Livre("il était une fois !", "stephen king", 1456789)
    print(livre.get_title())