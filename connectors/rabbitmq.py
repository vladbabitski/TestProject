import pika
import os


def publish_mock_data():
    # Define the mock data
    mock_data = [
        {"id": 1, "name": "Vladislav"},
        {"id": 2, "name": "Victoria"},
        {"id": 3, "name": "Svetlana"}
    ]

    # Connection parameters
    credentials = pika.PlainCredentials(os.getenv('LOGIN'), os.getenv('PASSWORD'))
    parameters = pika.ConnectionParameters(os.getenv('DB_ADDRESS'), credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Declare the queue
    queue_name = os.getenv("QUEUE_NAME")
    channel.queue_declare(queue=queue_name)

    # Publish mock data to the queue
    for data in mock_data:
        channel.basic_publish(exchange='', routing_key=queue_name, body=str(data))

    # Close the connection
    connection.close()
