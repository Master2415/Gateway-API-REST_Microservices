from database.connection import Connection
from models.Profile import Profile

database = Connection()

async def isEmailTaken(email):
    existing_profile = database.query(Profile).filter_by(email=email).first()
    return existing_profile is not None