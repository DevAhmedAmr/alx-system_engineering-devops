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
    fileName=f"{id}.csv"

    r = requests.get(f"{url}/users/{id}")
    EMPLOYEE_NAME = json.loads(r.text)["name"]

    r = requests.get(f"{url}/todos/?userId={id}")
    todo = json.loads(r.text)


    create_file_if_Not_Exist(fileName)
        
    for task in todo:
        data = f""" "{task["userId"]}","{EMPLOYEE_NAME}","{task["completed"]}","{task["title"]}" """.strip()
        save_csv(fileName,data)
        
            
    
def create_file_if_Not_Exist(file_Name):
    try:
        open(f"./{file_Name}", 'x')
    except FileExistsError:
        pass        
    
def save_csv(file_name,data):
        with open(f"./{file_name}","a") as file:
            file.write(data+"\n")
    
if __name__ == "__main__":
    Gather_data()
