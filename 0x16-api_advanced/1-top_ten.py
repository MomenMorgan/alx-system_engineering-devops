#!/usr/bin/python3
"""
queries the Reddit API
returns the number of subscribres
"""

import requests


def top_ten(subreddit):
    """
    queries the Reddit API
    returns the number of subscribres
    """

    Url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)

    res = requests.get(Url, allow_redirects=False,
                       headers={"User-Agent": "My-User-Agent"})

    data = res.json()

    if res.status_code >= 300:
        print("None")
    else:
        for child in data.get("data").get("children"):
            title = child.get("data").get("title")
            print(title)
