import psycopg2
from psycopg2 import Error, sql

from env_data import db_user, db_password, db_host, db_port, db_name


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


def db_create():
    # Подключение к PostgreSQL
    connection = psycopg2.connect(
            f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}"
        )

    # connection = psycopg2.connect(
    #     user=db_user,
    #     password=db_password,
    #     host=db_host,
    #     port=db_port
    # )

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
