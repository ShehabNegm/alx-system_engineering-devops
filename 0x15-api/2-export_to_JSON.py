#!/usr/bin/python3
"""using REST API"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":

    id = int(argv[1])
    file_name = argv[1] + ".json"
    url_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(url_users)

    user_name = user.json().get('username')

    tasks = requests.get(url_todo)

    j = {}
    data = []
    with open(file_name, 'w') as c:
        key = argv[1]
        for task in tasks.json():
            if task['userId'] == id:
                task_dict = {}
                task_dict["task"] = task['title']
                task_dict["completed"] = task["completed"]
                task_dict['username'] = user_name
                data.append(task_dict)
        j[key] = data
        c.write(str(j))
