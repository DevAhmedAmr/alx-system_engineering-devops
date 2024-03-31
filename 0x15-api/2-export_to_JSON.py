#!/usr/bin/python3
"""place holder"""
import csv
import json
import requests
import sys

"""place holder"""


def Gather_data():
    """get data from api"""
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    fileName = f"{id}.json"

    r = requests.get(f"{url}/users/{id}")
    EMPLOYEE_NAME = json.loads(r.text)["name"]

    r = requests.get(f"{url}/todos/?userId={id}")
    userName = json.loads(requests.get(f"{url}/users/?id={str(id)}").text)[0][
        "username"
    ]

    todo = json.loads(r.text)
    #####################
    dic = create_user_task_dict(username=userName, todo_list=todo)

    ########################

    create_file_if_Not_Exist(fileName)
    save_as_json(filename=fileName, dictionary=dic)


def create_file_if_Not_Exist(file_Name):
    try:
        open(f"./{file_Name}", "x")
    except FileExistsError:
        pass


def create_user_task_dict(todo_list: dict, username: str):

    user_dict = dict()

    if len(todo_list) < 1:
        print("empty todo_list in create_user_task_dict function")
        return None

    USER_ID = todo_list[0]["userId"]
    user_dict[USER_ID] = []

    for task in todo_list:
        task_dic = dict()
        task_dic["task"] = task["title"]
        task_dic["completed"] = task["completed"]
        task_dic["username"] = username
        user_dict[USER_ID].append(task_dic)

    return user_dict


def save_as_json(filename, dictionary: dict):
    dic = json.dumps(dictionary)
    with open(filename, "w") as file:
        file.write(dic)


if __name__ == "__main__":
    Gather_data()
