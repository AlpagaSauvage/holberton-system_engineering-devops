#!/usr/bin/python3
"""2-export_to_JSON.py"""

import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format
                        (id))
    task = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(id))

    ename = user.json()['username']
    eid = user.json()['id']
    jtask = task.json()

    udict = {eid: []}

    for ids in jtask:
        udict[eid].append({"task": ids['title'],
                           "completed": ids['completed'],
                           "username": ename})

    file = open("{}.json".format(eid), 'w')
    json.dump(udict, file)
    file.close()
