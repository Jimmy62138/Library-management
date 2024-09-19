from sqlite3 import IntegrityError

from InquirerPy import inquirer, get_style, prompt

from library import Library
from paper_book import PaperBook
from digital_book import DigitalBook
from menu import MENU
from users import Users

library = Library()


def get_menu() -> int:
    action = inquirer.select(
        message="Veuillez faire votre choix:",
        choices=MENU
    ).execute()
    return int(action[0])


def add_book() -> None:
    while True:
        isbn = inquirer.text(message="Entrez l'ISBN: ").execute()
        if isbn.isdigit():
            isbn = int(isbn)
            break
        print("Erreur, veuillez entrez des chiffres uniquement...")

    title: str = inquirer.text(message="Entrez le titre: ").execute()

    while True:
        autor = inquirer.text(message="Entrez l'auteur: ").execute()
        if not any(char.isdigit() for char in autor):
            break
        print("Erreur, le nom de l'auteur ne peux pas contenir de chiffres")

    genre: str = inquirer.select(message="Papier ou Numérique ?: ", choices=["Papier", "Numérique"]).execute()

    if genre == "Papier":
        library.add_book(PaperBook(isbn=isbn, title=title, autor=autor))
    else:
        library.add_book(DigitalBook(isbn=isbn, title=title, autor=autor))


def delete_book() -> None:
    books = library.get_all_books()
    if not books:
        print("La bibliothèque ne contient pas de livres.\n")
        return
    book = inquirer.select(
        message="Veuillez sélectionner le livre à supprimer:",
        choices=books
    ).execute()
    library.delete_book(book.get_isbn())


def print_books(books: list):
    print("*" * 70)
    for book in books:
        print(f"ISBN:{book.get_isbn()} | TITRE:{book.get_title()} | AUTEUR:{book.get_autor()} | TYPE:{book.get_type()}")
    print("*" * 70)


def search_books():
    
    if books := library.get_all_books():
        questions = [
            {
                "type": "fuzzy",
                "message": "Select actions:",
                "choices": books,
                "default": "",
                "max_height": "70%",
            }
        ]

        selected_book = prompt(questions=questions)[0]
        print_books([selected_book])

    else:
        print("La bibliothèque ne contient aucun livres.")


def add_user():
    while True:
        user_name = inquirer.text(message="Entez le nom du nouvel utilisateur: ").execute()
        if not any(char.isdigit() for char in user_name):
            break
        print("Erreur, le nom de l'utilisateur ne peux pas contenir de chiffres")
    user = Users(user_name)
    try:
        user.add_user()
    except IntegrityError:
        print(f"L'utilisateur {user_name} existe déja")


def show_books():
    print_books(library.get_all_books())


def borrow_book():
    books = library.get_available_books()
    users = library.get_users()

    if books and users:
        questions = [
            {
                "type": "fuzzy",
                "message": "Veuillez choisir le livre à emprunté:",
                "choices": books,
                "default": "",
                "max_height": "70%",
            }
        ]

        selected_book: DigitalBook | PaperBook | None = prompt(questions=questions)[0]

        questions = [
            {
                "type": "fuzzy",
                "message": "Veuillez choisir qui emprunte le livre:",
                "choices": users,
                "default": "",
                "max_height": "70%",
            }
        ]

        selected_user: Users | None = prompt(questions=questions)[0]
        library.borrow_book(selected_book, selected_user)

    else:
        print("La bibliothèque ne contient aucun livres disponible ou utilisateur.")


def return_book():
    books = library.get_unavailable_books()

    if books:
        questions = [
            {
                "type": "fuzzy",
                "message": "Veuillez choisir le livre à rendre:",
                "choices": books,
                "default": "",
                "max_height": "70%",
            }
        ]

        selected_book: DigitalBook | PaperBook | None = prompt(questions=questions)[0]
        library.return_book(selected_book)

    else:
        print("La bibliothèque ne contient aucun livres emprunté.")


def statistics():
    if books := library.get_statistics():
        print("*" * 70)
        for book in books:
            print(f"Titre: {book[0]} | Prêter: {book[1]} fois.")
        print("*" * 70)

    else:
        print("La bibliothèque ne contient aucun livres.")


def main():
    actions = {
        1: add_book,
        2: delete_book,
        3: search_books,
        4: add_user,
        5: borrow_book,
        6: return_book,
        7: show_books,
        8: statistics,
        9: exit
    }

    while True:
        choice = get_menu()
        action = actions.get(choice)
        action()


if __name__ == "__main__":
    main()
