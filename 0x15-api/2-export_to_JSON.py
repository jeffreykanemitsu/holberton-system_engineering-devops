#!/usr/bin/python3
'''
for a given employee ID, return info about his/her TODO list progress and
export data in JSON format
'''
import json
import requests
from sys import argv


if __name__ == "__main__":
    EMPLOYEE_ID = argv[1]
    URL = 'https://jsonplaceholder.typicode.com'
    USERNAME = requests.get(URL+'/users/'+EMPLOYEE_ID).json().get('username')
    TODO_LIST = requests.get(URL+'/todos?userId='+EMPLOYEE_ID).json()

    ALL_TASKS = []
    for task in TODO_LIST:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = USERNAME
        ALL_TASKS.append(task_dict)

    with open('{}.json'.format(EMPLOYEE_ID), 'w') as f:
        json.dump({EMPLOYEE_ID: ALL_TASKS}, f)
