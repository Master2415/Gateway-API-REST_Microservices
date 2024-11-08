import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import logging

host = os.getenv("PS_DATABASE_URL", "localhost")
user = os.getenv("PS_USER", "admin")
password = os.getenv("PS_PASSWORD", "12345")
dbname = os.getenv("PS_DBNAME", "profiles_db")
port = os.getenv("PS_PORT", "5432")

DSN = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
engine = create_engine(DSN)
Session = sessionmaker(bind=engine)

def Connection():
    return Session()

async def verifyDatabase():
    try:
        session = Session()
        session.execute(text('SELECT 1'))
        session.close()
        return True
    except Exception as e:
        logging.error(f"Failed to connect to database: {e}")
        return False
