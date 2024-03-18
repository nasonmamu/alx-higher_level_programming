#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to interact with the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database))

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query and delete states with names containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to interact with the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database))

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query and delete states with names containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
