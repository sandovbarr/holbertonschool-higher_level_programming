#!/usr/bin/python3
'''
    script that prints the first State
    object from the database hbtn_0e_6_usa
'''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, passwd, db_name))
    init_session = sessionmaker(bind=engine)
    conection = init_session()
    query_result = conection.query(State).first()
    if query_result:
        print("{}: {}".format(query_result.id, query_result.name))
    else:
        print('Nothing')
    conection.close()
