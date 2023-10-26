#!/usr/bin/env python3

import connexion

from db_store.db_connection import create_db_table
from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Book Inventory System - OpenAPI 3.0'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    create_db_table()
    main()
