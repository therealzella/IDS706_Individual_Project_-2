import sqlite3
import os

def connect_to_db(db_name="test.db"):
    """
    Connect to an SQLite database.
    """
    try:
        conn = sqlite3.connect(db_name)
        print(f"Connected to the database: {db_name}")
        return conn
    except Exception as e:
        print(f"Failed to connect to the database. Error: {e}")
        return None

def create_table(conn):
    """
    Create a users table if it doesn't exist.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            age INTEGER)''')
        conn.commit()
        print("Table 'users' created successfully.")
    except Exception as e:
        print(f"Failed to create table. Error: {e}")

if __name__ == "__main__":
    # Print the current working directory
    print(f"Current working directory: {os.getcwd()}")

    # Connect to the database and create a table
    conn = connect_to_db()
    
    if conn:
        create_table(conn)
        conn.close()
        print(f"Connection to the database is closed. Check if the file 'test.db' exists.")
    else:
        print("No connection to the database could be established.")

