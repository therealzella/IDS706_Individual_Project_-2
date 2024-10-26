# IDS706_Individual_Project_-2

This repository is for the IDS706 Individual Project #2, and the repository is built on previous one using Python for basic SQL queries.

![CI](https://github.com/therealzella/IDS706-python-github-template/actions/workflows/ci.yml/badge.svg)

## Features
- **SQLite Database Integration**: Supports CRUD operations.
- **Optimized Binary**: The project includes a GitHub Actions workflow to build and upload an optimized Rust binary.
- **GitHub Actions**: Automated CI/CD workflow to test, build, and upload artifacts.
- **Video Demo**: [Link to Video Demo](https://youtu.be/ggfInyxQE-4) 

## LLM Utilization
I utilized an LLM (Language Learning Model) to assist with various stages of the project, including:

- **Code Generation and Syntax Guidance**: The LLM helped with generating initial code structure in Rust, particularly as I'm relatively new to the language. It provided suggestions on Rust-specific syntax and the correct usage of libraries like `rusqlite` for database operations.
  
- **Debugging**: During debugging, the LLM was used to identify common errors and provide insights into fixing issues related to database handling and optimizing performance.

- **Optimization**: For improving the performance of my code, the LLM suggested strategies to efficiently use Rust’s memory and processing capabilities. This led to cleaner and more efficient code, ultimately contributing to the optimized binary build.

## Installation
To set up this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/therealzella/IDS706_Individual_Project_-2.git
    ```

2. Navigate to the project directory:
    ```sh
    cd IDS706_Individual_Project_-2
    ```

3. Create a virtual environment (optional but recommended):
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```sh
    make install

    ```
## Usage
### Prerequisites
- Rust
- SQLite

### Running the Program
To run the CLI, use the following commands:

```bash
# To create a record
cargo run create <name> <value>

# To read a record
cargo run read <id>

# To update a record
cargo run update <id> <value>

# To delete a record
cargo run delete <id>
