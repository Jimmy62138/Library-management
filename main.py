from sqlite3 import IntegrityError

from InquirerPy import inquirer, get_style, prompt

from book import Livre
from library import Bibliotheque
from paper_book import LivrePapier
from digital_book import LivreNumerique
from menu import MENU
from users import Utilisateur

# STYLE = get_style({"pointer": "blue"}, style_override=False)
library = Bibliotheque()


def get_menu() -> int:
    action = inquirer.select(
        message="Veuillez faire votre choix:",
        choices=MENU
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
        if not any(char.isdigit() for char in autor):
            break
        print("Erreur, le nom de l'auteur ne peux pas contenir de chiffres")

    genre: str = inquirer.select(message="Papier ou Numérique ?:",choices=["Papier", "Numérique"]).execute()

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
        choices=books
    ).execute()
    library.delete_book(book.get_isbn())


def print_books(books: list):
    print("*" * 23)
    for book in books:
        print(f"isbn:{book.get_isbn()}  titre:{book.get_title()}  auteur:{book.get_autor()}  type:{book.get_type()}")
    print("*" * 23)


def search_book():
    books = library.get_books()
    if books:
        books_title = [book.get_title() for book in books]

        questions = [
            {
                "type": "fuzzy",
                "message": "Select actions:",
                "choices": books_title,
                "default": "",
                "max_height": "70%",
            }
        ]

        selected_book = prompt(questions=questions)[0]
        for book in books:
            if book.get_title() == selected_book:
                print(f"ISBN: {book.get_isbn()}  TITLE: {book.get_title()}  AUTEUR: {book.get_autor()}  TYPE: {book.get_type()}")
                break
    else:
        print("La bibliothèque ne contient aucun livres.")




def add_user():
    while True:
        user_name = inquirer.text(message="Entez le nom du nouvel utilisateur: ").execute()
        if not any(char.isdigit() for char in user_name):
            break
        print("Erreur, le nom de l'utilisateur ne peux pas contenir de chiffres")
    user = Utilisateur("Jimmy")
    try:
        user.add_user()
    except IntegrityError:
        print(f"L'utilisateur {user_name} existe déja")


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
