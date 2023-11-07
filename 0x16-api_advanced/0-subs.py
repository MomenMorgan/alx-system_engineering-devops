#!/usr/bin/python3
"""
queries the Reddit API
returns the number of subscribres
"""

import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API
    returns the number of subscribres
    """

    Url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    res = requests.get(Url, allow_redirects=False)

    if res.status_code == 200:
        data = res.json()
        data = data.get('data').get('subscribers')
        if data == None:
            return 0
        else:
            return data
