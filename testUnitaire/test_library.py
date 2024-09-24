import pytest

from library import Library
from paper_book import PaperBook
from users import Users


@pytest.fixture
def library():
    return Library(db="../database/database.db")


@pytest.fixture
def book():
    return PaperBook(0000000000, "Livre de test", "moi")


@pytest.fixture
def user():
    return Users("user_test")


def test_add_book(library, book):
    library.add_book(book)
    inserted_book = library.get_a_book(book.get_isbn())[0]
    assert inserted_book.get_title() == "Livre de test"


def test_update_book(library, book):
    book.set_title("Livre de test 2")
    library.update_book(book, book.get_isbn())
    updated_book = library.get_a_book(book.get_isbn())[0]
    assert updated_book.get_title() == "Livre de test 2"


def test_get_a_book(library, book):
    assert library.get_a_book(book.get_isbn()) is not []


def test_get_all_books(library):
    assert library.get_all_books() is not []


def test_get_available_books(library):
    assert library.get_available_books() is not []


def test_add_user(user):
    user.DB = "../database/database.db"
    user.add_user()


def test_borrow_book(library, book, user):
    library.borrow_book(book, user)


def test_get_unavailable_books(library):
    unavailable_book = library.get_unavailable_books()[0]
    assert unavailable_book.get_title() == 'Livre de test 2'


def test_return_book(library, book):
    assert library.return_book(book) is True


def test_delete_book(library, book):
    library.delete_book(book.get_isbn())
    assert library.get_a_book(book.get_isbn()) == []


def test_get_users(library):
    assert library.get_users() is not []


def test_delete_user(library, user):
    library.delete_user(user)
