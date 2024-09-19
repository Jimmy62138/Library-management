import pytest

from book import Book


def test_book_instantiation():
    with pytest.raises(SyntaxError):
        book = Book(7896512365, "A title", "An autor")


if __name__ == "__main__":
    test_book_instantiation()

