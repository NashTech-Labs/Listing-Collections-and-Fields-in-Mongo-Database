# MongoDB Schema Explorer

This script allows you to explore the schema of a MongoDB database. It connects to a MongoDB instance using PyMongo and retrieves information about databases, collections, and fields (columns) within each collection.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your system (Python 3 recommended)
- PyMongo library installed (`pip install pymongo`)

## Usage

1. **Configuration**: Open the script `explore_mongodb_schema.py` in a text editor and provide the necessary MongoDB connection information:

    ```python
    # MongoDB connection information
    host = ''        # Replace with your MongoDB host
    port =           # Replace with your MongoDB port
    username = ''    # Replace with your MongoDB username
    password = ''    # Replace with your MongoDB password
    ```

2. **Running the Script**: To run the script, execute the following command in your terminal or command prompt:

    ```bash
    python <file-name>
    ```

    This will connect to the specified MongoDB instance, retrieve the schema information, and display it in the console.
