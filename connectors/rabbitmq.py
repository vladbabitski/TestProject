import pika

# Define the mock data
mock_data = [
    {"id": 1, "name": "Vladislav"},
    {"id": 2, "name": "Victoria"},
    {"id": 3, "name": "Svetlana"}
]

# Connection parameters
credentials = pika.PlainCredentials('login', 'pass')
parameters = pika.ConnectionParameters('127.0.0.1', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare the queue
queue_name = 'test_queue'
channel.queue_declare(queue=queue_name)

# Publish mock data to the queue
for data in mock_data:
    channel.basic_publish(exchange='', routing_key=queue_name, body=str(data))

# Close the connection
connection.close()
