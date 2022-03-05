#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(db)
    Session = sessionmaker(bind=db)
    session = Session()
    state = session.query(State).filter_by(name=argv[4]).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
