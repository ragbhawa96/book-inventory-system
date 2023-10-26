import logging

import connexion
import six

from db_store.mysql_db import MySqlDb
from swagger_server.models.book import Book  # noqa: E501
from swagger_server.models.book_creation_request import BookCreationRequest  # noqa: E501
from swagger_server import util

db_service = MySqlDb()


def create_book(body=None):  # noqa: E501
    """Create book

    This can only be done by the logged in book. # noqa: E501

    :param body: Created book object
    :type body: dict | bytes

    :rtype: Book
    """
    # if connexion.request.is_json:
    #     body = BookCreationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'
    try:

        result = db_service.add_book(title=body.get("title"),
                                     isbn=body.get("isbn"),
                                     price=body.get("price"),
                                     book_count=body.get("book_count"))
        if result:
            return result, 201
        else:
            return None, 400
    except Exception as exc:
        logging.error(str(exc))


def delete_book(book_id):  # noqa: E501
    """Delete book

    Delete an book # noqa: E501

    :param book_id: The bookID that needs to be deleted
    :type book_id: str

    :rtype: None
    """
    try:
        result = db_service.delete_book(book_id=book_id)
        if result:
            return "Book deleted successfully!", 204
        else:
            return "Book Not Found!", 404
    except Exception as exc:
        logging.error(str(exc))


def get_book(book_id):  # noqa: E501
    """Get book by book ID

     # noqa: E501

    :param book_id: The book ID that needs to be fetched. Use book1 for testing. 
    :type book_id: int

    :rtype: Book
    """
    try:
        result = db_service.get_book_by_id(book_id=book_id)
        if result:
            response = Book(book_id=result.book_id,
                            title=result.title,
                            isbn=result.isbn,
                            price=result.price,
                            book_count=result.book_count)
            return response, 200
        else:
            return "Book not found!", 404
    except Exception as exc:
        logging.error(str(exc))


def get_books():  # noqa: E501
    """Get all books

     # noqa: E501


    :rtype: List[Book]
    """
    try:
        result = db_service.get_books()
        if result:
            response: list[Book] = [
                Book(book_id=book.book_id,
                     title=book.title,
                     isbn=book.isbn,
                     price=book.price,
                     book_count=book.book_count)
                for book in result
            ]
            return response, 200
        else:
            return "Books not found!", 404
    except Exception as exc:
        logging.error(str(exc))


def update_book(book_id, body=None):  # noqa: E501
    """Update book

    Update book details # noqa: E501

    :param book_id: bookId that need to be updated
    :type book_id: int
    :param body: Update an existent book
    :type body: dict | bytes

    :rtype: Book
    """
    # if connexion.request.is_json:
    #     body = BookCreationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!'
    try:

        result = db_service.update_book(book_id=book_id,
                                        title=body.get("title"),
                                        isbn=body.get("isbn"),
                                        price=body.get("price"),
                                        book_count=body.get("book_count"))
        if result:
            return result, 201
        else:
            return None, 400
    except Exception as exc:
        logging.error(str(exc))
