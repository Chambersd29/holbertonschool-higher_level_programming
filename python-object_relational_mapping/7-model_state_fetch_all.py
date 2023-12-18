#!/usr/bin/python3
"""
Este módulo se conecta a MySql a través sqlalchmemy(ORM).
Realiza uan consulta SELECT states en hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Esta validación es para evitar que el archivo
    se ejecute al import, Se realiza la una consulta SELECT
    a los campos id y name en states en hbtn_0e_6_usa.
    """

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@{host}:{port}/{db_name}',
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id.asc()).all()

    for state in states:
        print(f'{state.id}: {state.name}')
