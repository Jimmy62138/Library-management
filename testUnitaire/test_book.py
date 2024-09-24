import pytest

from book import Book
from book import normalizer


@pytest.fixture()
def book():
    return Book(7896512365, "a title", "an author")


def test_normalizer():
    assert normalizer("énorme Python ç'est la vie.") == "enorme Python c'est la vie."


def test_book_isbn(book):
    assert book.get_isbn() == 7896512365


def test_book_title(book):
    assert book.get_title() == "A title"


def test_book_author(book):
    assert book.get_author() == "An Author"


def test_set_title(book):
    book.set_title("un autre titre")
    assert book.get_title() == "Un autre titre"


def test_set_author(book):
    book.set_author("un autre auteur")
    assert book.get_author() == "Un Autre Auteur"
