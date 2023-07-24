#!/usr/bin/python3
"""
This module contains solutions to API Project
tasks.
We are pulling and using APIs from
"https://jsonplaceholder.typicode.com"
"""
import re
import requests
import sys

# define the API url
API = "https://jsonplaceholder.typicode.com"


def main():
    """show how many of how many tasks is done by user
    User id is passed as an argument"""
    if len(sys.argv) > 1:
        id = sys.argv[1]
        if re.fullmatch(r"\d+", sys.argv[1]):
            emp_res = requests.get('{}/users/{}'.format(API, id)).json()
            emp_name = emp_res['name']
            emp_todos = requests.get(
                '{}/users/{}/todos'.format(API, id)).json()
            completed_todos = requests.get(
                '{}/users/{}/todos?completed=true'.format(API, id)).json()
            no_todos = len(emp_todos)
            no_completed = len(completed_todos)
        print(
            'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    no_completed,
                    no_todos
                    )
            )
        for todo in completed_todos:
            print(f"\t {todo['title']}")


if __name__ == '__main__':
    main()
