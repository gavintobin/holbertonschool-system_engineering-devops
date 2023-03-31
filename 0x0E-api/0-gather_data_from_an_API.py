#!/usr/bin/python3

import requests
import sys
import urllib

if __name__ == '__main__':

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

    # Count the number of completed tasks and the total number of tasks
    num_completed_tasks = 0
    total_num_tasks = len(todos)
    completed_tasks = []

    for todo in todos:
        if todo['completed']:
            num_completed_tasks += 1
            completed_tasks.append(todo['title'])

    # Get the employee's name
    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']

    # Display the TODO list progress
    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, num_completed_tasks, total_num_tasks))

    # Display the completed task titles
    for task in completed_tasks:
        print(f"\t {task}")
