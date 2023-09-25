#!/usr/bin/python3
"""using REST API"""

import requests
from sys import argv
import json


if __name__ == "__main__":

    id = int(argv[1])
    url_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(url_users)

    user_name = user.json().get('name')

    tasks = requests.get(url_todo)
    total = 0
    done = 0
    tasks_done = []
    for task in tasks.json():
        if task['userId'] == id:
            if task['completed'] is True:
                done += 1
                tasks_done.append(task['title'])
            total += 1

    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          done,
                                                          total))
    for i in tasks_done:
        print("\t {}\n".format(i), end="")
