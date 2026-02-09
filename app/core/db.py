from pymongo import MongoClient
from .config import settings

_client = None

def get_client() -> MongoClient:
    global _client
    if _client is None:
        _client = MongoClient(settings.MONGO_URI)
    return _client

def get_db():
    return get_client()[settings.DB_NAME]
