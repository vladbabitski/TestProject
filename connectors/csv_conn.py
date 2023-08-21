import csv
import logging

def process_mock_data():
    # Define the mock data
    mock_data = [
        {"id": 1, "name": "Vladislav"},
        {"id": 2, "name": "Victoria", "surname": "Babitskaya"},
        {"id": 3, "name": "Svetlana", "surname": "Babitskaya", "email": "testemail@test.com"}
    ]

    # Write the mock data to a CSV file
    filename = "test_data.csv"
    fieldnames = ["id", "name", "surname", "email"]

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in mock_data:
            writer.writerow(row)

    # Read the mock data from the CSV file
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            logging.info(f"mock data from csv file:\n{row}")


def get_mock_data_by_attribute(attribute, attribute_value):
    # Read the mock data from the CSV file and search for the data with the given ID
    with open("test_data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row[attribute]) == attribute_value:
                return row
    return None

# Get mock data by any attribute (in this example - id)
def test_get_mock_data_by_id(attribute: str = 'id', attribute_value: int = 2):
    # Call the method to process the mock data
    process_mock_data()
    data = get_mock_data_by_attribute(attribute, attribute_value)
    if data is not None:
        logging.info(f"Mock data with ID {attribute_value}: {data}")
    else:
        logging.warning(f"Mock data with ID {attribute_value} not found!")


test_get_mock_data_by_id()
