import psycopg2
import logging
from psycopg2 import Error, sql

from env_data import db_user, db_password, db_host, db_port, db_name


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
#
# Base = declarative_base()
# Session = sessionmaker(bind=engine)
# session = Session()

logger = logging.getLogger("Connect_database")


# class ConnectionDBContexManager:
# # def __init__(self, schema_name: str) -> None:
# #     """
# #     :param schema_name: the db schema (i.e. the tenant)
# #     """
# #     super().__init__()
# #     self.schema_name = schema_name
#
#     def __init__(self) -> None:
#         self.connection = None
#
#     def __enter__(self):
#         try:
#             self.connection = psycopg2.connect(
#                 f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}"
#             )
#             print(self.connection)
#             return self.connection
#         except psycopg2.OperationalError as err:
#         # except Error as err:
#             logger.info("Connect_database: ", err)
#             return err
#
#             # pass
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("-"*100, self.connection)
#         # logger.error("Connect_database: " )
#         print("-"*100, exc_tb)
#         if self.connection:
#             self.connection.commit()
#             self.connection.close()


from contextlib import closing

def cursor_db():
    connection = psycopg2.connect(
                    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}"
                )
    with closing(connection) as conn:
        return conn
        # with conn.cursor() as cursor:
        #     return cursor




def conn_db():
    connection = psycopg2.connect(
        f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}"
    )


def create_db():
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


def run_database_query(query: str):
    connection = psycopg2.connect(
                    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
                )
    with closing(connection) as connect:
        with connect.cursor() as cursor:
            db_create = psycopg2.sql.SQL(query)
            cursor.execute(db_create)
        connect.commit()
        connect.close()


# from django.contrib.auth.models import User

# user = User.objects.all()
# print(user)


# run_database_query("INSERT INTO auth_group (name) VALUES ('operator');")
# run_database_query("DELETE FROM auth_group WHERE name = 'operator';")


