#!/usr/bin/python3
"""
Este módulo de prueba sirve para conectar
con MySQL
"""


import MySQLdb
import sys


def main():
    """
    Esta función hace la consulta de la
    tabla states en hbtn_0e_0_usa.
    """

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        port=3306,
        database=sys.argv[3],
    )
    r = db.cursor()
    r.execute("SELECT * FROM states ORDER BY id ASC")
    rows = r.fetchall()

    for row in rows:
        print(row)

    r.close()
    db.close()


if __name__ == "__main__":
    """
    Esta validación evita que se ejecute
    este archivo.
    """
    main()
