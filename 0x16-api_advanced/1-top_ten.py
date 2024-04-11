#!/usr/bin/python3
"""dependencies"""
import requests, json


def top_ten(subreddit):
    """a function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""
    number_of_titles = 0
    r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )
    Data: dict = r.json()
    if r.status_code == 200:
        for i in range(len(Data["data"]["children"])):
            print(Data["data"]["children"][i]["data"]["title"])
            number_of_titles += 1
    else:
        print(None)
    print(number_of_titles)


if "__main__" == __name__:
    top_ten("programming")
