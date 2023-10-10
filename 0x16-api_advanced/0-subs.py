#!/usr/bin/python3
# using reddit api

import requests


def number_of_subscribers(subreddit):
    """function to return numbers of subs of subreddit using reddit api"""

    url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)
    header = {'User-agent': 'shehab'}
    try:
        r = requests.get(url, headers=header)
        j = r.json()
        return j["data"]["children"][0]["data"]["subreddit_subscribers"]
    except Exception:
        return 0
