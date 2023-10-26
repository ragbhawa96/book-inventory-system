from sqlalchemy import create_engine, Column, String, MetaData, Integer
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import DeclarativeBase

engine = None

# Create the metadata object
metadata = MetaData()


class Base(DeclarativeBase):
    pass


class BookData(Base):
    __tablename__ = 'book'
    book_id = Column("book_id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String(255))
    isbn = Column("isbn", String(255), unique=True)
    # isbn = Column("isbn", String(255))
    price = Column("price", String(255))
    book_count = Column("book_count", Integer)

    def __repr__(self):
        return f"Book: {self.title}, isbn: {self.isbn}"


def create_db_table():
    try:
        global engine
        engine = create_engine("mysql+pymysql://root:password@localhost:3306/books_db", echo=True)
    except SQLAlchemyError as e:
        raise e

    try:
        if not database_exists(engine.url):
            create_database(engine.url)
        BookData.metadata.create_all(engine)
    except SQLAlchemyError as e:
        raise e
