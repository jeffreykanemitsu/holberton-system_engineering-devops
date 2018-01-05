#!/usr/bin/python3
'''
export data in JSON format
'''
import json
import requests


if __name__ == "__main__":
    URL = 'https://jsonplaceholder.typicode.com'
    EMPLOYEE = requests.get(URL+'/users').json()
    TODO_LIST = requests.get(URL+'/todos').json()
    RECORDS = {}

    for e in EMPLOYEE:
        EMPLOYEE_ID = e.get('id')
        USERNAME = e.get('username')

        for task in TODO_LIST:
            if (task.get('userId') == int(EMPLOYEE_ID)):
                task_dict = {}
                task_dict['task'] = task.get('title')
                task_dict['completed'] = task.get('completed')
                task_dict['username'] = USERNAME
                TODO_LIST.append(task_dict)

        RECORDS[EMPLOYEE_ID] = TODO_LIST

    with open('todo_all_employees.json', 'w') as f:
        json.dump(RECORDS, f)
