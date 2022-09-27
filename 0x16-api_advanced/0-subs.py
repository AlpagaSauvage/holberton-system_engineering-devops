#!/usr/bin/python3
"""0-subs"""


import requests


def number_of_subscribers(subreddit):
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                            headers={'User-agent': 'Alpaga'})
    if response is None or response.status_code != 200:
        return 0

    response_data = response.json()['data']

    return response_data['subscribers']
