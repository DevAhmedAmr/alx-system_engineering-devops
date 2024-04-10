#!/usr/bin/python3

"""dependencies"""
import json
import sys


def number_of_subscribers(subreddit):
    import requests

    """function to return number of subscriber of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = {"User-Agent": "My-User-Agent"}
    r = requests.get(url, headers=user_agent, allow_redirects=False)

    # print(json.dumps(r))
    if r.status_code >= 300:
        return 0
    return r.json().get("data").get("subscribers")


if __name__ == "__main__":
    number_of_subscribers = __import__("0-subs").number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
