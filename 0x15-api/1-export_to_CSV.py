#!/usr/bin/python3
'''
for a given employee ID, return info about his/her TODO list progress and
export data in the CSV format
'''
import requests
from sys import argv
import csv


if __name__ == "__main__":
    EMPLOYEE_ID = argv[1]
    URL = 'https://jsonplaceholder.typicode.com'
    USERNAME = requests.get(URL + '/users/' + EMPLOYEE_ID).json().get('username')
    TODO_LIST = requests.get(URL + '/todos?userId=' + EMPLOYEE_ID).json()

    with open('{}.csv'.format(EMPLOYEE_ID), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in TODO_LIST:
            writer.writerow([EMPLOYEE_ID, USERNAME, task.get('completed'), task.get('title')])
