#!/usr/bin/python3
"""
extending task 0 to export to csv
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
            # get responses
            emp_res = requests.get('{}/users/{}'.format(API, id)).json()
            emp_name = emp_res['name']
            emp_todos = requests.get(
                '{}/users/{}/todos'.format(API, id)).json()
            # completed_todos = requests.get(
            #     '{}/users/{}/todos?completed=true'.format(API, id)).json()
            # no_todos = len(emp_todos)
            # no_completed = len(completed_todos)
            
            # write responses to csv
            with open('{}.csv'.format(id), 'w') as fp:
                for todo in emp_todos:
                    fp.write(
                        '"{}", "{}", "{}". "{}"\n'.format(
                            id,
                            emp_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                )


if __name__ == '__main__':
    main()
