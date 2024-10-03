import sqlite3

def connect_to_db(db_name="test.db"):
    """
    Connect to an SQLite database.
    """
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    """
    Create a users table if it doesn't exist.
    """
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        age INTEGER)''')
    conn.commit()

def insert_user(conn, name, age):
    """
    Insert a new user into the users table.
    """
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

def read_users(conn):
    """
    Retrieve all users from the users table.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def update_user(conn, user_id, new_name):
    """
    Update the name of a user by ID.
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, user_id))
    conn.commit()

def delete_user(conn, user_id):
    """
    Delete a user by ID from the users table.
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

if __name__ == "__main__":
    # Connect to the database
    conn = connect_to_db()

    # Create the table
    create_table(conn)

    # Insert some users
    insert_user(conn, "John Doe", 28)
    insert_user(conn, "Jane Smith", 32)

    # Read users
    print("Users in the database:")
    users = read_users(conn)
    for user in users:
        print(user)

    # Update a user
    print("\nUpdating John Doe's name to Johnny Doe.")
    user_id = users[0][0]  # Assuming John Doe is the first user
    update_user(conn, user_id, "Johnny Doe")

    # Read users again to see the update
    print("Users after update:")
    users = read_users(conn)
    for user in users:
        print(user)

    # Delete a user
    print("\nDeleting Jane Smith.")
    user_id = users[1][0]  # Assuming Jane Smith is the second user
    delete_user(conn, user_id)

    # Read users after deletion
    print("Users after deletion:")
    users = read_users(conn)
    for user in users:
        print(user)

    # Close the database connection
    conn.close()
