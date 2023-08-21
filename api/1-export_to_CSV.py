#!/usr/bin/python3
""" This module make beginner level API calls to a dummy data service"""
import csv
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

    # ----- Make a second api call for data on the user only
    api_url = base_url + s + users + s + employee_id
    response = requests.get(api_url)
    user_dict = response.json()

    # ----- Create variables for csv creation
    username = user_dict.get('username')

    # Create a list of dictionaries of required data to send to csv writer
    list_keys = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    list_values = []
    formatted_data_dict = {}
    list_of_data_dictionaries = []
    for todo in user_todo_list:
        completion_status = todo.get('completed')
        task_name = todo.get('title')
        list_values.append(employee_id)
        list_values.append(username)
        list_values.append(completion_status)
        list_values.append(task_name)
        formatted_data_dict = dict(zip(list_keys, list_values))
        list_of_data_dictionaries.append(formatted_data_dict)
        list_values.clear()

    # ----- Create the CSV file
    f = open("{}.csv".format(employee_id), 'w+')
    csv_file = csv.writer(
        f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for item in list_of_data_dictionaries:
        csv_file.writerow(item.values())
