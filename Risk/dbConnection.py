from sqlalchemy import Connection, create_engine, text
from typing import Optional

# singleton connection, if there use it, if not then establish
username = "postgres"
password = "postgres123"
host = "localhost"
port = "5432"
database = "Risk"

# Create connection string
connection_string = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
engine = create_engine (connection_string)
conn 

def close_db_connection():
    global conn
    if conn is not None and conn.closed == 0:
        conn.close()
        print("Database connection closed.")


def insert_into_DB(table, columns, values):
    query = "Insert into" + table + " ( "+ columns + ") values( " + ','.join(values) +")"
    global conn 
    if conn is None:
        conn = connectToDB()
    
    
def connectToDB():
# Replace with your actual connection info
# place credentials at a safe location
    username = "postgres"
    password = "postgres123"
    host = "localhost"
    port = "5432"
    database = "Risk"

    # Create connection string
    connection_string = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"

    # Create SQLAlchemy engine
    engine = create_engine(connection_string)
    global conn 
    conn = engine.connect() 
    return conn is not None


def query(statement : str):
    global conn 
    if conn is  None:
        conn = connectToDB()
    result = conn.execute(text("SELECT * from test;"))
    print(result.fetchone())
    close_db_connection()

if __name__ == "__main__":
    print("hello world")
    try:
        conn = connectToDB()
    
    finally:
        close_db_connection()
        print("Connection closed")