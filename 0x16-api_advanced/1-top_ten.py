#!/usr/bin/python3
"""1-top_ten"""

import requests


def top_ten(subreddit):
    request = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                           .format(subreddit),
                           headers={"User-Agent": "holberton"},
                           allow_redirects=False)

    if request.status_code == 200:
        for k in request.json().get("data").get("children"):
            print(k.get("data").get("title"))
    else:
        print(None)
