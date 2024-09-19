from paper_book import PaperBook


def test_support_type():
    book = PaperBook(7896512365, "a title", "an autor")
    assert book.get_type() == "papier"