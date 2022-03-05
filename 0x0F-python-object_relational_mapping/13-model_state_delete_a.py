#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
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
    states_a = session.query(State).filter(State.name.like('%a%'))
    for state in states_a:
        session.delete(state)
    session.commit()
    session.close()
