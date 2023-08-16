from pymongo import MongoClient

# Define the mock data
mock_data = [
    {"id": 1, "name": "Vladislav"},
    {"id": 2, "name": "Victoria"},
    {"id": 3, "name": "Svetlana"}
]

# Connection parameters
client = MongoClient('mongodb://127.0.0.1')
db = client['test_db_name']  # Specify the database name
collection = db['my_collection']  # Specify the collection name

# Insert mock data into the collection
collection.insert_many(mock_data)

# Close the connection
client.close()