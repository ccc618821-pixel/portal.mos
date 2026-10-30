from contextlib import contextmanager
import psycopg2
from config import db_host, db_name, db_pass, db_port, db_user
@contextmanager
def open_connection():
    connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_pass,
        port=db_port
    )
    try:
        yield connection
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()