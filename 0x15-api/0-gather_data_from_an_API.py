#!/usr/bin/python3
'''for a given employee ID, return info about his/her TODO list progress'''
import requests
from sys import argv


if __name__ == "__main__":
    EMPLOYEE_ID = argv[1]
    URL = 'https://jsonplaceholder.typicode.com'
    USER = requests.get(URL + '/users/' + EMPLOYEE_ID).json().get('name')
    TODO_LIST = requests.get(URL + '/todos?userId=' + EMPLOYEE_ID).json()

    TASKS_DONE = []
    TOTAL_TASKS = 0
    TASKS_COMPLETED = 0

    for task in TODO_LIST:
        if task.get('userId') == int(EMPLOYEE_ID):
            TOTAL_TASKS += 1
            if task.get('completed'):
                TASKS_COMPLETED += 1
                TASKS_DONE.append(task.get('title'))

    print('Employee {} is done with tasks({:d}/{:d}):'.format(USER, TASKS_COMPLETED, TOTAL_TASKS))

    for completed in TASKS_DONE:
        print('\t {:s}'.format(completed)) 
