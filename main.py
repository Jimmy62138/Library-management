from sqlite3 import IntegrityError

from InquirerPy import inquirer, prompt

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
    return action[:2]


def add_book() -> None:
    """
    Prompts the user to enter the ISBN, title, author, and genre of the book, validates the input, and adds the book to
    the library.
    """
    while True:
        isbn = inquirer.text(message="Entrez l'ISBN: ").execute()
        if isbn.isdigit():
            isbn = int(isbn)
            break
        print("Erreur, veuillez entrez des chiffres uniquement...")

    title: str = inquirer.text(message="Entrez le titre: ").execute()

    while True:
        author = inquirer.text(message="Entrez l'auteur: ").execute()
        if not any(char.isdigit() for char in author):
            break
        print("Erreur, le nom de l'auteur ne peux pas contenir de chiffres")

    genre: str = inquirer.select(message="Papier ou Numérique ?: ", choices=["Papier", "Numérique"]).execute()

    book_class = PaperBook if genre == "Papier" else DigitalBook
    library.add_book(book_class(isbn=isbn, title=title, author=author))


def update_book():
    """
    Allows the user to update the details of a book in the library.
    """
    if books := library.get_all_books():
        book = inquirer.select(
            message="Quel livre voulez vous modifier ?:",
            choices=books
        ).execute()

        isbn = book.get_isbn()
        attribute = inquirer.select(
            message="Quel voulez vous modifier ?:",
            choices=["ISBN", "TITRE", "AUTEUR", "TYPE"]
        ).execute()

        if attribute == "ISBN":
            while True:
                new_isbn = inquirer.text(message="Entrez le nouvel ISBN: ").execute()
                if new_isbn.isdigit():
                    new_isbn = int(new_isbn)
                    break
                print("Erreur, veuillez entrez des chiffres uniquement...")

            book.set_isbn(new_isbn)
        elif attribute == "TITRE":
            title = inquirer.text(message="Entrez le nouveau titre: ").execute()
            book.set_title(title)

        elif attribute == "AUTEUR":
            while True:
                author = inquirer.text(message="Entrez un nouveau nom d'auteur: ").execute()
                if not any(char.isdigit() for char in author):
                    break
                print("Erreur, le nom de l'auteur ne peux pas contenir de chiffres")
            book.set_author(author)
        else:
            support: str = inquirer.select(message="Papier ou Numérique ?: ", choices=["Papier", "Numérique"]).execute()
            book.set_type(support)

        library.update_book(book, isbn)

    else:
        print("La bibliothèque ne contient pas de livres.")


def delete_book() -> None:
    """
    Deletes a book from the library by prompting the user to select a book to delete.
    """
    books = library.get_all_books()
    if not books:
        print("La bibliothèque ne contient pas de livres.")
        return
    book = inquirer.select(
        message="Veuillez sélectionner le livre à supprimer:",
        choices=books
    ).execute()
    library.delete_book(book.get_isbn())


def print_books(books: list):
    """
    Prints the details of the books provided in a formatted manner.

    Args:
        books (list): A list of books to print.
    """
    if books:
        print("\n" + "*" * 70)
        for book in books:
            print(f"ISBN:{book.get_isbn()} | TITRE:{book.get_title()} | AUTEUR:{book.get_author()} | TYPE:{book.get_type()}")
        print("*" * 70 + "\n")
    else:
        print("\nLa bibliothèque ne contient aucun livres.\n")


def search_books():
    """
    Searches for books in the library and prints the details of the selected book.
    """
    if books := library.get_all_books():
        questions = [
            {
                "type": "fuzzy",
                "message": "Sélectionner un livre.:",
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
    """
    Adds a new user to the library by prompting the user to enter the user's name.
    """
    while True:
        user_name = inquirer.text(message="Entez le nom du nouvel utilisateur: ").execute()
        if not any(char.isdigit() for char in user_name):
            break
        print("Erreur, le nom de l'utilisateur ne peux pas contenir de chiffres")
    user = Users(user_name)
    try:
        user.add_user()
    except IntegrityError:
        print(f"Erreur, l'utilisateur {user_name} existe déja")


def delete_user():
    """
    Deletes a user from the library by prompting the user to select a user to delete.
    """
    if users := library.get_users():
        questions = [
            {
                "type": "fuzzy",
                "message": "Veuillez choisir l'utilisateur à supprimer':",
                "choices": users,
                "default": "",
                "max_height": "70%",
            }
        ]
        selected_user: Users | None = prompt(questions=questions)[0]
        library.delete_user(selected_user)

    else:
        print("La bibliothèque ne contient aucun utilisateur.")


def show_books():
    """
    Displays all books in the library.
    """
    print_books(library.get_all_books())


def borrow_book():
    """
    Allows a user to borrow a book from the library.
    """
    books = library.get_available_books()
    users = library.get_users()

    if not users:
        print("La bibliothèque ne contient aucun utilisateur, veuillez en ajouté un.")
    elif not books:
        print("La bibliothèque ne contient aucun livres disponible.")
    else:
        questions = [
            {
                "type": "fuzzy",
                "message": "Veuillez choisir un livre à emprunté:",
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


def return_book():
    """
    Allows a user to return a borrowed book to the library.
    """
    if books := library.get_unavailable_books():
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
    """
    Displays the statistics of books loans.
    """
    if books := library.get_statistics():
        print("\n" + "*" * 70)
        for book in books:
            print(f"Titre: {book[0]} | Prêter: {book[1]} fois.")
        print("*" * 70 + "\n")
    else:
        print("La bibliothèque ne contient aucun livres.")


def main():
    actions = {
        "01": add_book,
        "02": update_book,
        "03": delete_book,
        "04": search_books,
        "05": add_user,
        "06": delete_user,
        "07": borrow_book,
        "08": return_book,
        "09": show_books,
        "10": statistics,
        "00": exit
    }

    while True:
        choice = get_menu()
        action = actions.get(choice)
        action()


if __name__ == "__main__":
    main()
