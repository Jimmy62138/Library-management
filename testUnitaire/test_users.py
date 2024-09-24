import pytest

from users import Users


@pytest.fixture
def setup_db():
    Users.DB = "../database/database.db"


@pytest.fixture
def user(setup_db):
    return Users("test_user")


def test_add_user(user):
    user.add_user()
    assert user.get_user() == [('Test_user',)]


def test_get_name(user):
    assert user.get_name() == "Test_user"


def test_delete_user(user):
    user.delete_user()
    assert user.get_user() == []

