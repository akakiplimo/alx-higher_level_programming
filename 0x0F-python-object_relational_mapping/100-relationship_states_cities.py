#!/usr/bin/python3
"""
script that creates the State 'California' with the City 'San Francisco'
from the database hbtn_0e_100_usa
"""


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # required arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (mysql_username, mysql_password, database_name),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state_city = State(name="California",
                           cities=[City(name="San Francisco")])
    session.add(new_state_city)
    session.commit()
    session.close()
