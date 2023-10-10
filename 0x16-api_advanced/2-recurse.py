#!/usr/bin/python3
"""using reddit API"""

import requests


def recurse(subreddit, hot_list=[], after="null"):
    """function to return all hot titles of subreddit using reddit api"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-agent': 'shehab'}
    par = {"limit": "100", "after": after}
    r = requests.get(url, headers=header, params=par)
    j = r.json()
    if r.status_code != 200:
        return None

    else:
        for posts in j['data']['children']:
            post = posts['data']['title']
            hot_list.append(post)
        after = j['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
