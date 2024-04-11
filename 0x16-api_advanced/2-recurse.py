#!/usr/bin/python3
import json
import requests
import sys


def recurse(subreddit, hot_list: list = [], after=None):
    """a function that queries the Reddit API and return a list
    of all  hot posts titles  for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after} if after else {"limit": 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    for child in data["data"]["children"]:
        hot_list.append(child["data"]["title"])

    if data["data"].get("after") is not None:
        return recurse(subreddit, hot_list, data["data"]["after"])

    return hot_list


# Data["data"]["children"][i]["data"]["title"]


if __name__ == "__main__":
    recurse = __import__("2-recurse").recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
