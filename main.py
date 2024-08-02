from paper_book import LivrePapier
from digital_book import LivreNumerique
from menu import MENU

def main():
    pass

if __name__ == "__main__":
    livre = LivreNumerique("L'attaque des clones", "George Lucas", 1383472345)
    print(livre.get_autor())
    print(livre)
    
    livre = LivrePapier("the lost symbol", "Dan Brown", 987656789)
    print(livre.get_autor())
    print(livre)