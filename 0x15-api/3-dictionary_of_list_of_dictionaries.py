#!/usr/bin/python3
"""place holder"""
import csv
import json
import requests
import sys

"""place holder"""


def Gather_data():
    """get data from api"""
    url = "https://jsonplaceholder.typicode.com"
    fileName = "todo_all_employees.json"




    r = requests.get(f"{url}/todos")

    todo = json.loads(r.text)
    #####################
    dic = create_user_task_dict( Users_todo_list=todo)

    ########################
    create_file_if_Not_Exist(fileName)
    save_as_json(filename=fileName, dictionary=dic)


def create_file_if_Not_Exist(file_Name):
    try:
        open(f"./{file_Name}", "x")
    except FileExistsError:
        pass


def create_user_task_dict(Users_todo_list: dict):

    users_dict = dict()
    users=dict()
    for task in Users_todo_list:
        user_id = task["userId"]
        url = "https://jsonplaceholder.typicode.com"
        
        if users.get(user_id) is None:
            userName = json.loads(requests.get(f"{url}/users/?id={str(user_id)}").text)[0][
                "username"
            ]
        else:
            userName = users[user_id]
            
        users[user_id] =userName
        
        
        if user_id not in users_dict:
            users_dict[user_id] = []

        user_task_dict = dict()

        user_task_dict["task"] = task["title"]
        user_task_dict["completed"] = task["completed"]
        user_task_dict["username"] = userName
        users_dict[user_id].append(user_task_dict)

    return users_dict


def save_as_json(filename, dictionary: dict):
    dic = json.dumps(dictionary)
    with open(filename, "w") as file:
        file.write(dic)


if __name__ == "__main__":
    Gather_data()
