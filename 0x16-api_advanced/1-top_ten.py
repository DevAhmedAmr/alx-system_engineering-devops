#!/usr/bin/python3
"""dependencies"""
import requests, json


def top_ten(subreddit):
    """a function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""

    r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )
    Data: dict = r.json()
    if r.status_code == 200:
        for i in range(len(Data["data"]["children"])):
            print(Data["data"]["children"][i]["data"]["title"])
    else:
        print(None)


if "__main__" == __name__:
    top_ten("programming")
