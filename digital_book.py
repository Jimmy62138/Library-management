from book import Livre

class LivreNumerique(Livre):
    
    def __init__(self, title: str, autor: str, isbn: int) -> None:
        super().__init__(title=title, autor=autor, isbn=isbn)
        self.__type = "numerique"
        
    def __str__(self) -> str:
        return self.get_title()
        
    def get_type(self) -> str:
        return self.__type
        