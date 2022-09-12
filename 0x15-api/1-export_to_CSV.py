#!/usr/bin/python3
"""1-export_to_CSV.py"""

import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    html = 'https://jsonplaceholder.typicode.com/users/'
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format
                        (id))
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(id))
    uname = user.json()['username']
    uid = user.json()['id']
    jtask = tasks.json()

    fcsv = open('{}.csv'.format(uid), 'w')
    writer = csv.writer(fcsv, delimiter=",", quotechar='"',
                        quoting=csv.QUOTE_ALL)

    for ids in jtask:
        writer.writerow([uid, uname, ids['completed'], ids['title']])
    fcsv.close()
