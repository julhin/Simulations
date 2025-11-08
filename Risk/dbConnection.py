from sqlalchemy import create_engine, text

# singleton connection, if there use it, if not then establish
conn = None
def close_db_connection():
    global conn
    if conn is not None and conn.closed == 0:
        conn.close()
        conn = None
        print("Database connection closed.")



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
    return engine.connect() 


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
        connectToDB()
    finally:
        close_db_connection()
        print("Connection closed")