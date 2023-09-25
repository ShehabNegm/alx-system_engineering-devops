#!/usr/bin/python3
"""using REST API"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":

    id = int(argv[1])
    file_name = argv[1] + ".csv"
    url_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(url_users)

    user_name = user.json().get('username')

    tasks = requests.get(url_todo)

    with open(file_name, 'w') as c:
        writer = csv.writer(c, quoting=csv.QUOTE_ALL, quotechar='"')
        for task in tasks.json():
            if task['userId'] == id:
                writer.writerow([task['userId'], user_name,
                                 task['completed'], task['title']])
