#!/usr/bin/python3
import requests
import json
import sys

"""dependencies"""
myUser_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
user_agent = {"User-Agent": myUser_agent}


def number_of_subscribers(subreddit):
    """function to return number of subscriber of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    r = requests.get(
        url,
        headers=user_agent,
    )

    # print(json.dumps(r))
    if r.status_code == 200:
        return r.json()["data"]["subscribers"]
    return 0


if __name__ == "__main__":
    x = number_of_subscribers(sys.argv[1])
    print(x)
