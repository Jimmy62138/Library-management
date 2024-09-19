import pytest

from book import Book
from book import normalizer


@pytest.fixture()
def book():
    return Book(7896512365, "a title", "an autor")


def test_normalizer():
    assert normalizer("énorme Python ç'est la vie.") == "enorme Python c'est la vie."


def test_book_isbn(book):
    assert book.get_isbn() == 7896512365


def test_book_title(book):
    assert book.get_title() == "A title"


def test_book_autor(book):
    assert book.get_autor() == "An Autor"


def test_set_title(book):
    book.set_title("un autre titre")
    assert book.get_title() == "Un autre titre"


def test_set_autor(book):
    book.set_autor("un autre auteur")
    assert book.get_autor() == "Un Autre Auteur"
