# Library
## Docstring project around POO


Library is a project made with Python that aims to manage a library of books and users.

## Features

- Books management
    - add a book
    - delete a book
    - update a book
    - search a book
- Users management
    - add user
    - delete user
- borrowing books
- return a book
- disaplay all books
- statistics
- Save fonctionality into Sqlite3 database

> The main goal of this library is to learn object-oriented programming with Python.
> This includes object-oriented programming, unit testing, comments and docstrings.

## Tech

The library uses a number of the following open source projects:

- [Python3] - Programming language
- [Sqlite3] - Lite SQL database
- [InquirerPy] - Embeddable and beautiful command line interface
- [pytest] - For unit test
- [pytest-html] - To generate an HTML view of unit test results.
- [coverage] - Display Unit Test Coverage

## Installation

Library requires [Python3](https://www.python.org/) to run.

Install the dependencies and start the program.

```sh
pip install -r requirements.txt
Python3 main.py
```


**On first start the code will automatically create a database with 2 empty SQL tables: Books and Users**

| Documentations        | Path                                  |
|-----------------------|---------------------------------------|
| Users                 | UserID (integer) unique autoincrement |
|                       | Name   (varchar) not null             |
| --------------------- | ------------------------------------  |
| Books                 | Isbn   (interger) unique not null     |
|                       | Title  (varchar)  not null            |
|                       | Author (varchar)  not null            |
|                       | Type   (varchar)  not null            |
|                       | Lend   (interger) default 0           |
|                       | UserID (int)      default null        |



## Documentations

| Documentations     | Path                             |
|--------------------|----------------------------------|
| DocString (Sphinx) | /docs/_build/html/index.html     |
| Pytest result      | /testUnitaire/index.html         |
| Tests coverage     | /testUnitaire/htmlcov/index.html |


JIMMY

**Free Software, Hell Yeah!**