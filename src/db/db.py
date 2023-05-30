import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        return psycopg2.connect(
            dbname = 'playes',
            user= 'postgres',
            password= 'jade12',
            port='6000'
        )
    except DatabaseError as ex:
        raise ex