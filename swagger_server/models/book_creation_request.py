# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BookCreationRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, title: str=None, isbn: str=None, price: str=None, book_count: int=None):  # noqa: E501
        """BookCreationRequest - a model defined in Swagger

        :param title: The title of this BookCreationRequest.  # noqa: E501
        :type title: str
        :param isbn: The isbn of this BookCreationRequest.  # noqa: E501
        :type isbn: str
        :param price: The price of this BookCreationRequest.  # noqa: E501
        :type price: str
        :param book_count: The book_count of this BookCreationRequest.  # noqa: E501
        :type book_count: int
        """
        self.swagger_types = {
            'title': str,
            'isbn': str,
            'price': str,
            'book_count': int
        }

        self.attribute_map = {
            'title': 'title',
            'isbn': 'isbn',
            'price': 'price',
            'book_count': 'book_count'
        }
        self._title = title
        self._isbn = isbn
        self._price = price
        self._book_count = book_count

    @classmethod
    def from_dict(cls, dikt) -> 'BookCreationRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The bookCreationRequest of this BookCreationRequest.  # noqa: E501
        :rtype: BookCreationRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self) -> str:
        """Gets the title of this BookCreationRequest.

        The title of the book  # noqa: E501

        :return: The title of this BookCreationRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this BookCreationRequest.

        The title of the book  # noqa: E501

        :param title: The title of this BookCreationRequest.
        :type title: str
        """

        self._title = title

    @property
    def isbn(self) -> str:
        """Gets the isbn of this BookCreationRequest.

        The ISBN of the book  # noqa: E501

        :return: The isbn of this BookCreationRequest.
        :rtype: str
        """
        return self._isbn

    @isbn.setter
    def isbn(self, isbn: str):
        """Sets the isbn of this BookCreationRequest.

        The ISBN of the book  # noqa: E501

        :param isbn: The isbn of this BookCreationRequest.
        :type isbn: str
        """

        self._isbn = isbn

    @property
    def price(self) -> str:
        """Gets the price of this BookCreationRequest.

        The price of the book  # noqa: E501

        :return: The price of this BookCreationRequest.
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price: str):
        """Sets the price of this BookCreationRequest.

        The price of the book  # noqa: E501

        :param price: The price of this BookCreationRequest.
        :type price: str
        """

        self._price = price

    @property
    def book_count(self) -> int:
        """Gets the book_count of this BookCreationRequest.

        The available number of books  # noqa: E501

        :return: The book_count of this BookCreationRequest.
        :rtype: int
        """
        return self._book_count

    @book_count.setter
    def book_count(self, book_count: int):
        """Sets the book_count of this BookCreationRequest.

        The available number of books  # noqa: E501

        :param book_count: The book_count of this BookCreationRequest.
        :type book_count: int
        """

        self._book_count = book_count