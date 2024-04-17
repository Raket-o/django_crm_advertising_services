import logging
from contextlib import closing

import psycopg2
from psycopg2 import Error, sql

from env_data import db_host, db_name, db_password, db_port, db_user

logger = logging.getLogger("Connect_database")


def create_db():
    connection = psycopg2.connect(
            f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}"
        )

    try:
        cursor = connection.cursor()
        connection.autocommit = True
        db_create = psycopg2.sql.SQL(f'CREATE DATABASE {db_name}')
        cursor.execute(db_create)
        cursor.close()

    except Error:
        pass

    finally:
        if connection:
            connection.close()
