from InquirerPy import inquirer, get_style

from library import Bibliotheque
from paper_book import LivrePapier
from digital_book import LivreNumerique
from menu import MENU

STYLE = get_style({"pointer": "blue"}, style_override=False)
library = Bibliotheque()


def get_menu() -> int:
    action = inquirer.select(
        message="Veuillez faire votre choix:",
        choices=MENU, style=STYLE
    ).execute()
    return int(action[0])


def add_book() -> None:
    while True:
        isbn = inquirer.text(message="Entez l'ISBN:").execute()
        if isbn.isdigit():
            isbn = int(isbn)
            break
        print("Erreur, veuillez entrez des chiffres uniquement")

    title: str = inquirer.text(message="Entrez le titre:").execute()

    while True:
        autor = inquirer.text(message="Entez l'auteur:").execute()
        if not any (char.isdigit() for char in autor):
            break
        print("Erreur, le nom de l'auteur ne peux pas contenir de chiffres")

    genre: str = inquirer.select(message="Papier ou Numérique ?:",choices=["Papier", "Numérique"], style=STYLE).execute()

    if genre == "Papier":
        library.add_book(LivrePapier(isbn=isbn, title=title, autor=autor))
    else:
        library.add_book(LivreNumerique(isbn=isbn, title=title, autor=autor))


def delete_book() -> None:
    books = library.get_books()
    if not books:
        print("La bibliothèque ne contient pas de livres.\n")
        return
    book = inquirer.select(
        message="Veuillez sélectionner le livre à supprimer:",
        choices=books, style=STYLE
    ).execute()
    library.delete_book(book.get_isbn())


def search_book():
    pass


def add_user():
    pass


def show_books():
    [print(book) for book in library.get_books()]


def main():
    actions = {
        1: add_book,
        2: delete_book,
        3: search_book,
        4: add_user,
        5: lambda: print("You can become a mobile app developer"),
        6: lambda: None,
        7: show_books,
        8: lambda: None,
        9: exit
    }

    while True:
        choice = get_menu()
        action = actions.get(choice)
        action()


if __name__ == "__main__":
    main()
    #livre = LivrePapier(987656789, "the lost symbol", "Dan Brown")
    #library.add_book(livre)
    #print(livre)
    #livre.set_title("mars attack")
    #library.update_book(livre)
    # library.delete_book(livre)
