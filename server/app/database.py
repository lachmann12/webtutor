from databases import Database
from sqlalchemy import create_engine
from .models import Base

import json

def read_config():
    f = open('../secrets/config.json')
    return json.load(f)

db_info = read_config()["database"]
print(db_info)

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(db_info["user"], db_info["password"], db_info["host"], db_info["port"], db_info["dbname"])
print(SQLALCHEMY_DATABASE_URL)

database = Database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base.metadata.create_all(bind=engine)