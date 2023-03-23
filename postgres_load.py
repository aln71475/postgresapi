import psycopg2
import pandas as pd
from sqlalchemy import create_engine

def readdb():
    conn_string = 'postgresql://john:password@localhost/accounts_db'
    db = create_engine(conn_string)
    conn = db.connect()
    dbdf = pd.read_sql("select * from newaccounts",conn)
    # print(dbdf)
    dfdict = dbdf.to_dict(orient='records')
    return dbdf