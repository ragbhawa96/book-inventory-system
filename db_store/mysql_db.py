import logging
from sqlalchemy.orm import sessionmaker
from db_store.db_connection import engine, BookData
from swagger_server.models import Book


class MySqlDb:
    def __init__(self):
        self.session = sessionmaker(bind=engine)()

    def add_book(self, title, isbn, price, book_count):
        book = None
        try:
            new_book = BookData(title=title,
                                isbn=isbn,
                                price=price,
                                book_count=book_count)
            self.session.add(new_book)
            self.session.commit()

            book_id = new_book.book_id
            print(book_id)
            self.session.close()

            book = Book(book_id=book_id, title=title, isbn=isbn, price=price, book_count=book_count)
            return book
        except Exception as exc:
            logging.error(str(exc))
            self.session.rollback()
            self.session.close()
            return book

    def get_book_by_id(self, book_id):
        book = BookData()
        try:
            book = self.session.query(BookData).get(book_id)
            self.session.close()
            return book
        except Exception as exc:
            logging.error(str(exc))
            return book

    def get_books(self):
        books = None
        try:
            books = self.session.query(BookData).all()
            self.session.close()
            return books
        except Exception as exc:
            logging.error(str(exc))
            return books

    def update_book(self, book_id, title, isbn, price, book_count):
        book = Book()
        try:
            book = self.session.query(BookData).get(book_id)
            if book:
                book.title = title
                book.isbn = isbn
                book.price = price
                self.session.commit()
            self.session.close()

            book = Book(book_id=book_id, title=title, isbn=isbn, price=price, book_count=book_count)
            return book
        except Exception as exc:
            logging.error(str(exc))
            self.session.close()
            return book

    def delete_book(self, book_id):
        try:
            book = self.session.query(BookData).get(book_id)
            if book:
                self.session.delete(book)
                self.session.commit()
                self.session.close()
                return True
            else:
                logging.info("userNot Found!")
                return False
        except Exception as exc:
            logging.error(str(exc))
            self.session.close()
            return False
