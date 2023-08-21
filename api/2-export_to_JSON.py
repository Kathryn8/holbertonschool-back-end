#!/usr/bin/python3
""" This module make beginner level API calls to a dummy data service"""
import csv
import requests
import sys
import json

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

    # ----- Make a second api call for data on the user only
    api_url = base_url + s + users + s + employee_id
    response = requests.get(api_url)
    user_dict = response.json()

    # ----- Create variables for csv creation
    username = user_dict.get('username')

    # Create a list of dictionaries of required data to send to csv writer
    list_keys = ["task", "completed", "username"]
    list_values = []
    formatted_data_dict = {}
    list_of_data_dictionaries = []
    for todo in user_todo_list:
        completion_status = todo.get('completed')
        task_name = todo.get('title')
        list_values.append(task_name)
        list_values.append(completion_status)
        list_values.append(username)
        formatted_data_dict = dict(zip(list_keys, list_values))
        list_of_data_dictionaries.append(formatted_data_dict)
        list_values.clear()
    new_dict = {str(employee_id): list_of_data_dictionaries}

    # ----- Create the json file
    with open("{}.json".format(employee_id), 'w+') as f:
        f.write(json.dumps(new_dict))
