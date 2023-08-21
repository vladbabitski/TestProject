from pymongo import MongoClient
import os
from query.json_data import (json_data_example)


def insert_mock_data_into_db():
    # Define the mock data
    mock_data = [
        {"id": 1, "name": "Vladislav"},
        {"id": 2, "name": "Victoria"},
        {"id": 3, "name": "Svetlana"}
    ]

    # Connection parameters
    client = MongoClient(os.getenv('mongo_db_address'))
    db = client[os.getenv('mongo_db_name')]  # Specify the database name
    collection = db[os.getenv('collection_name')]  # Specify the collection name

    # Insert mock data into the collection
    collection.insert_many(mock_data)

    # Close the connection
    client.close()


def send_json_to_mongodb(json_data):
    # Establish a connection to MongoDB
    client = MongoClient(os.getenv('mongo_db_address'))

    # Access the desired database and collection
    db = client[os.getenv('mongo_db_name')]  # Specify the database name
    collection = db[os.getenv('collection_name')]  # Specify the collection name

    # Insert the JSON data into the collection
    collection.insert_one(json_data)

    # Close the MongoDB connection
    client.close()


# Call the method to send the JSON data to MongoDB
send_json_to_mongodb(json_data_example)
