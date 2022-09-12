#!/usr/bin/python3
"""0-gather_data_from_an_API"""

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    html = 'https://jsonplaceholder.typicode.com/users/'
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format
                        (id))
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(id))
    ename = user.json()['name']
    jtask = tasks.json()
    todolist = []
    nbtasks = 0
    alltasks = 0

    for ids in jtask:
        if ids['completed'] is True:
            todolist.append(ids['title'])
            nbtasks += 1
        alltasks += 1

    print("Employee {} is done with tasks({}/{}):".format(ename, nbtasks,
                                                          alltasks))

    for todo in todolist:
        print("\t {}".format(todo))
