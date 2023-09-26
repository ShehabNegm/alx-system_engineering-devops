#!/usr/bin/python3
"""using REST API"""

import json
from collections import OrderedDict
import requests


if __name__ == "__main__":

    file_name = "todo_all_employees.json"
    url_users = 'https://jsonplaceholder.typicode.com/users/'
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(url_users)

    user_name = user.json().get('username')

    tasks = requests.get(url_todo)

    j = OrderedDict()
    data = []
    id = 1
    with open(file_name, 'w+') as c:
        key = str(id)
        for task in tasks.json():
            if task['userId'] == str(id):
                task_dict = OrderedDict()
                task_dict["task"] = task['title']
                task_dict["completed"] = task["completed"]
                task_dict['username'] = user_name
                data.append(task_dict)
        j[key] = data
        json.dump(j, c)
