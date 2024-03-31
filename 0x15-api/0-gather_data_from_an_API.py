#!/usr/bin/python3
"""place holder"""

import json
import requests
import sys

"""place holder"""


def Gather_data():
    """get data from api"""
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    r = requests.get(f"{url}/users/{id}")
    EMPLOYEE_NAME = json.loads(r.text)["name"]

    r = requests.get(f"{url}/todos/?userId={id}")

    NUMBER_OF_DONE_TASKS = 0
    todo = json.loads(r.text)
    TOTAL_NUMBER_OF_TASKS = len(todo)
    for task in todo:

        if task["userId"] == int(id):

            if task["completed"] is True:
                NUMBER_OF_DONE_TASKS += 1

    print(
        "Employee {} is done with tasks ({}/{}):".format(
            EMPLOYEE_NAME, TOTAL_NUMBER_OF_TASKS, NUMBER_OF_DONE_TASKS
        )
    )
    for task in todo:
        if task["completed"] is True:
            print("\t ", task["title"])


if __name__ == "__main__":
    Gather_data()
