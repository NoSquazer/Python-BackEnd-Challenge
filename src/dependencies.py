# SrcUtilities
from src.database.connection import get_db_connection


def get_db():
    db_connection = get_db_connection()
    return db_connection
