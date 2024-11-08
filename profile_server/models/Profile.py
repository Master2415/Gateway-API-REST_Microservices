from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base()

class Profile(Model):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    url = Column(String(255))
    nickname = Column(String(255))
    public_info = Column(String(255))
    messaging = Column(String(255))
    biography = Column(String(255))
    organization = Column(String(255))
    country = Column(String(255))
    social_media = Column(String(255))
    email = Column(String(255), unique=True)
