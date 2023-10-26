# Book Inventory System

## Overview
This service provides an APIs for managing book inventory. It exposes the following endpoints:

- /books: Get a list of all books.
- /books/{book_id}: Get the details of a specific book.
- /books: Add a new book.
- /books/{book_id}: Update the details of a specific book.
- /books/{book_id}: Delete a specific book.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```


To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```