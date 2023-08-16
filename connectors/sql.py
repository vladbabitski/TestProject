import sqlite3

# Define the mock data
mock_data = [
    (1, 'Vladislav'),
    (2, 'Victoria'),
    (3, 'Svetlana')
]

# Create a connection to the SQLite database
conn = sqlite3.connect('db_name.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table to store the mock data
cursor.execute('''CREATE TABLE IF NOT EXISTS test_table 
                  (id INTEGER PRIMARY KEY, name TEXT)''')

# Insert the mock data into the table
cursor.executemany('INSERT INTO test_table VALUES (?, ?)', mock_data)

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()
