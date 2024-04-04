from pymongo import MongoClient
from pymongo.errors import OperationFailure

# MongoDB connection information
host = ''   #enter the host
port = ''   # enter port
username = ''  # Replace with your MongoDB username
password = ''  # Replace with your MongoDB password

# Connect to MongoDB with authentication
try:
    client = MongoClient(host=host, port=port, username=username, password=password)
    print("Connected successfully!")
except OperationFailure as e:
    print(f"Failed to connect: {e}")
    exit()

# Get list of databases
databases = client.list_database_names()

# Iterate over each database
for db_name in databases:
    if db_name == 'config':  # Skip 'config' database
        print(f"Skipping database: {db_name} (system database)")
        continue
    print(f"Database: {db_name}")
    db = client[db_name]
    
    # Get list of collections (tables)
    collections = db.list_collection_names()
    
    # Iterate over each collection
    for collection_name in collections:
        print(f"\tCollection: {collection_name}")
        collection = db[collection_name]
        
        # Get sample document to extract field names (column names)
        sample_document = collection.find_one()
        
        if sample_document:
            # Extract field names (column names)
            field_names = sample_document.keys()
            print("\t\tFields:")
            for field_name in field_names:
                print(f"\t\t\t{field_name}")
        else:
            print("\t\tNo documents found in collection.")
