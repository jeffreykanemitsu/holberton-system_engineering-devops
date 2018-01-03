#!/usr/bin/python3
'''for a given employee ID, return info about his/her TODO list progress'''
import requests
from sys import argv


if __name__ == "__main__":
    EMPLOYEE_ID = argv[1]
    URL = 'https://jsonplaceholder.typicode.com'
    EMPLOYEE_NAME = requests.get(URL+'/users/'+EMPLOYEE_ID).json().get('name')
    TODO_LIST = requests.get(URL+'/todos?userId='+EMPLOYEE_ID).json()

    TASKS_DONE = []
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    for task in TODO_LIST:
        if task.get('userId') == int(EMPLOYEE_ID):
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get('completed'):
                NUMBER_OF_DONE_TASKS += 1
                TASKS_DONE.append(task.get('title'))

    print('Employee {} is done with tasks({:d}/{:d}):'.format(EMPLOYEE_NAME,
          NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for completed in TASKS_DONE:
        print('\t {:s}'.format(completed))
