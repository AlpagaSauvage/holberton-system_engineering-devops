#!/usr/bin/python3
"""2-rescurse"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    if after is None:
        return

    response = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit),
                            headers={'User-agent': 'Alpaga'},
                            params={'after': after})
    if response is None or response.status_code != 200:
        return None

    data = response.json()['data']
    for article in data['children']:
        hot_list.append(article)
    recurse(subreddit, hot_list, data['after'])

    return hot_list
