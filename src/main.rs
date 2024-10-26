use rusqlite::{params, Connection, Result};
use std::env;

fn main() -> Result<()> {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("Usage: cargo run <command> [arguments]");
        println!("Commands:");
        println!("  create <name> <value>    - Add a new record");
        println!("  read <id>               - Read a record by ID");
        println!("  update <id> <value>     - Update a record by ID");
        println!("  delete <id>             - Delete a record by ID");
        return Ok(());
    }

    // Establish a connection to the SQLite database
    let conn = Connection::open("database.db")?;

    // Initialize the table (only needs to be done once)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            value TEXT NOT NULL
        )",
        [],
    )?;

    // Determine the command
    match args[1].as_str() {
        "create" => {
            if args.len() < 4 {
                println!("Usage: create <name> <value>");
            } else {
                let name = &args[2];
                let value = &args[3];
                create_record(&conn, name, value)?;
                println!("Record created successfully.");
            }
        }
        "read" => {
            if args.len() < 3 {
                println!("Usage: read <id>");
            } else {
                let id: i32 = args[2].parse().expect("ID should be an integer");
                read_record(&conn, id)?;
            }
        }
        "update" => {
            if args.len() < 4 {
                println!("Usage: update <id> <value>");
            } else {
                let id: i32 = args[2].parse().expect("ID should be an integer");
                let new_value = &args[3];
                update_record(&conn, id, new_value)?;
                println!("Record updated successfully.");
            }
        }
        "delete" => {
            if args.len() < 3 {
                println!("Usage: delete <id>");
            } else {
                let id: i32 = args[2].parse().expect("ID should be an integer");
                delete_record(&conn, id)?;
                println!("Record deleted successfully.");
            }
        }
        _ => println!("Unknown command. Use create, read, update, or delete."),
    }

    Ok(())
}

// CRUD functions

fn create_record(conn: &Connection, name: &str, value: &str) -> Result<usize> {
    conn.execute(
        "INSERT INTO records (name, value) VALUES (?1, ?2)",
        params![name, value],
    )
}

fn read_record(conn: &Connection, id: i32) -> Result<()> {
    let mut stmt = conn.prepare("SELECT id, name, value FROM records WHERE id = ?1")?;
    let mut rows = stmt.query(params![id])?;

    if let Some(row) = rows.next()? {
        let id: i32 = row.get(0)?;
        let name: String = row.get(1)?;
        let value: String = row.get(2)?;
        println!("ID: {}, Name: {}, Value: {}", id, name, value);
    } else {
        println!("Record not found.");
    }

    Ok(())
}

fn update_record(conn: &Connection, id: i32, new_value: &str) -> Result<usize> {
    conn.execute(
        "UPDATE records SET value = ?1 WHERE id = ?2",
        params![new_value, id],
    )
}

fn delete_record(conn: &Connection, id: i32) -> Result<usize> {
    conn.execute("DELETE FROM records WHERE id = ?1", params![id])
}

