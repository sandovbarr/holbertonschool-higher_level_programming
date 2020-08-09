#!/usr/bin/python3
''' script that lists all states from the database hbtn_0e_0_usa '''


import MySQLdb
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    ''' Empty class that inherits from Base '''
    tablename = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
