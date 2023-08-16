import csv

# Define the mock data
mock_data = [
    {"id": 1, "name": "Vladislav"},
    {"id": 2, "name": "Victoria"},
    {"id": 3, "name": "Svetlana"}
]

# Write the mock data to a CSV file
filename = "test_data.csv"
fieldnames = ["id", "name"]

with open(filename, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in mock_data:
        writer.writerow(row)

# Read the mock data from the CSV file
with open(filename, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

