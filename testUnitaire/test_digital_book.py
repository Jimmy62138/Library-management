from digital_book import DigitalBook


def test_support_type():
    book = DigitalBook(7896512365, "a title", "an autor")
    assert book.get_type() == "numerique"
