#!/usr/bin/python3
""" This module make beginner level API calls to a dummy data service"""
import requests
import sys

if __name__ == '__main__':

    # ----- Exit script with error message if no arguments given
    try:
        if not sys.argv[1]:
            pass
    except IndexError:
        sys.exit("This script requires an argument of employee_id number")

    # ----- Define components of api_url string
    employee_id = str(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    s = "/"
    users = "users"
    todos = "todos"

    # ----- Make api call to users with their todos
    api_url = base_url + s + users + s + employee_id + s + todos
    response = requests.get(api_url)
    user_todo_list = response.json()

    # ----- Extract a list of completed tasks from user-todo api call
    completed_task_list = []
    for user_todo_dict in user_todo_list:
        if user_todo_dict.get('completed') is True:
            completed_task_list.append(user_todo_dict.get('title'))

    # ----- Make a second api call for data on the user only
    api_url = base_url + s + users + s + employee_id
    response = requests.get(api_url)
    user_dict = response.json()

    # ----- Create variables for print display
    employee_name = user_dict.get('name')
    no_completed_tasks = len(completed_task_list)
    no_total_tasks = len(user_todo_list)

    # ----- Display data to standard output
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, no_completed_tasks, no_total_tasks))
    for task in completed_task_list:
        print(f"\t {task}")
