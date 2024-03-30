#!/usr/bin/python3
"""
place holder
"""

import requests
import sys
import json
"""
place holder
"""
def Gather_data():
	"""_summary_
	"""
	id = sys.argv[1]

	r = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
	EMPLOYEE_NAME =json.loads( r.text)["name"]

	r = requests.get(f'https://jsonplaceholder.typicode.com/todos/?userId={id}')

	NUMBER_OF_DONE_TASKS=0
	todo=json.loads( r.text)
	TOTAL_NUMBER_OF_TASKS=len(todo)
	for task in todo:
		
		if task["userId"]==int(id):
			
			if task["completed"]== True:
				NUMBER_OF_DONE_TASKS+=1
				
	print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

	for task in todo:
		if task["completed"] == True:
			print(" ","\t",task["title"])
if __name__ == "__main__":
    Gather_data()