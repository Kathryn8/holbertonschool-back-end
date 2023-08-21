#!/usr/bin/python3
""" This module make beginner level API calls to a dummy data service"""
import json
import requests

if __name__ == '__main__':

    # ----- Define components of api_url string
    base_url = "https://jsonplaceholder.typicode.com"
    s = "/"
    users = "users"
    todos = "todos"

    # ----- Make api call to retrieve a list of user dictionaries
    api_url = base_url + s + users
    response = requests.get(api_url)
    user_list = response.json()

    # Grab from the user list a list of their id numbers
    username_id_list = []
    for item in user_list:
        username_id_list.append((item.get('id'), item.get('username')))

    # ----- Make a second api call for all todos
    api_url = base_url + s + todos
    response = requests.get(api_url)
    total_todo_list = response.json()

    # Create a list of dictionaries of required data to write json file
    new_dict = {}
    for (user_id, username) in username_id_list:
        list_of_dicts = []
        for todo in total_todo_list:
            if user_id == todo.get('userId'):
                completion_status = todo.get('completed')
                task_name = todo.get('title')
                dict_of_todos = {
                    "username": username,
                    "task": task_name,
                    "completed": completion_status
                }
                list_of_dicts.append(dict_of_todos)
        new_dict[user_id] = list_of_dicts

    # ----- Create the json file
    with open("todo_all_employees.json", 'w+') as f:
        f.write(json.dumps(new_dict))
