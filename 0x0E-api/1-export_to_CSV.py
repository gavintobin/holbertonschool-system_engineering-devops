#!/usr/bin/python3
'''task 1'''
import requests
import csv
import sys

# Define the base URL for the API
base_url = 'https://jsonplaceholder.typicode.com'

# Define the employee ID as a command-line argument
employee_id = sys.argv[1]

# Define the endpoint URL for the employee's TODO list
todo_url = f'{base_url}/todos?userId={employee_id}'

# Send a GET request to the TODO list endpoint
response = requests.get(todo_url)

# Parse the JSON response into a Python dictionary
todos = response.json()

# Get the employee's name
user_url = f'{base_url}/users/{employee_id}'
user_response = requests.get(user_url)
user_data = user_response.json()
employee_name = user_data['username']

# Define the CSV file name
csv_file_name = f'{employee_id}.csv'

# Write the TODO list to a CSV file
with open(csv_file_name, mode='w', newline='') as csv_file:
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for todo in todos:
        writer.writerow({
            'USER_ID': employee_id,
            'USERNAME': employee_name,
            'TASK_COMPLETED_STATUS': str(todo['completed']),
            'TASK_TITLE': todo['title']
        })

# Display a success message
print(f'TODO list for employee {employee_name} has been exported to {csv_file_name}')
