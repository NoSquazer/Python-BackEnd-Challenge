# PyMongo
from pymongo import MongoClient

# SrcUtilities
from src.config import settings


def get_db_connection():
    try:
        client = MongoClient(settings.MONGO_URI)
        db = client.challenge_set
        return db
    except Exception as error:
        print("Error connecting to the database:", str(error))
        return None
