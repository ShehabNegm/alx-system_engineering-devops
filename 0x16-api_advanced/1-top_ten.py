#!/usr/bin/python3
"""using reddit API"""

import requests


def top_ten(subreddit):
    """function to return top 10 hot titles of subreddit using reddit api"""

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-agent': 'shehab'}
    try:
        r = requests.get(url, headers=header)
        j = r.json()
        for posts in j['data']['children']:
            post = posts['data']['title']
            print(post)
    except Exception:
        print("None")
