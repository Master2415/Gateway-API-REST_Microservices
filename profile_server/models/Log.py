from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base()  

class Log(Model):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    app_name = Column(String(255))
    log_type = Column(String(255))
    module = Column(String(255))
    log_date_time = Column(String(255))
    summary = Column(String(255))
    description = Column(String(255))
