from library import Bibliotheque
from paper_book import LivrePapier
from digital_book import LivreNumerique
from menu import MENU

def main():
    pass

if __name__ == "__main__":
    
    library = Bibliotheque()
    livre = LivrePapier(987656789, "the lost symbol", "Dan Brown")
    library.add_book(livre)
    print(livre)
    livre.set_title("mars attack")
    library.update_book(livre)
    #library.delete_book(livre)