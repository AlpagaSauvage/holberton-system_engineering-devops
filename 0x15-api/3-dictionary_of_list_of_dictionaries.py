#!/usr/bin/python3
"""3-dictionary_of_list_of_dictionaries"""

import json
import requests

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users')

    juser = user.json()

    udict = {}

    for user in juser:
        uid = user['id']
        tasks = requests.get(
                       'https://jsonplaceholder.typicode.com/users/{}/todos'
                       .format(uid))

        jtask = tasks.json()

        udict[str(user['id'])] = []

        for ids in jtask:
            udict[str(user['id'])].append({"username": user['username'],
                                           "task": ids['title'],
                                           "completed": ids['completed']})

    file = open("todo_all_employees.json", 'w')
    json.dump(udict, file)
    file.close()
