import pytest
from main import connect_to_db, create_table, insert_user, read_users, update_user, delete_user

@pytest.fixture
def db_conn():
    conn = connect_to_db(":memory:")  # Use in-memory database for tests
    create_table(conn)
    yield conn
    conn.close()

def test_create_table(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    assert cursor.fetchone() is not None, "Table creation failed."

def test_insert_user(db_conn):
    insert_user(db_conn, "Test User", 25)
    users = read_users(db_conn)
    assert len(users) == 1
    assert users[0][1] == "Test User"
    assert users[0][2] == 25

def test_read_users(db_conn):
    insert_user(db_conn, "Alice", 30)
    insert_user(db_conn, "Bob", 35)
    users = read_users(db_conn)
    assert len(users) == 2
    assert users[0][1] == "Alice"
    assert users[1][1] == "Bob"

def test_update_user(db_conn):
    insert_user(db_conn, "Charlie", 40)
    users = read_users(db_conn)
    user_id = users[0][0]
    update_user(db_conn, user_id, "Charles")
    updated_users = read_users(db_conn)
    assert updated_users[0][1] == "Charles"

def test_delete_user(db_conn):
    insert_user(db_conn, "David", 45)
    users = read_users(db_conn)
    user_id = users[0][0]
    delete_user(db_conn, user_id)
    remaining_users = read_users(db_conn)
    assert len(remaining_users) == 0

