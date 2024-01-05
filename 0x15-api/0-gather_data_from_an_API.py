#!/usr/bin/python3
"""script that returns information about an employee TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    userid = int(sys.argv[1])
    user = '{}users/{}'.format(url, userid)
    res = requests.get(user)
    json_res = res.json()
    name = json_res.get('name')

    todos = '{}todos?userId={}'.format(url, userid)
    res_todos = requests.get(todos)
    tasks = res_todos.json()
    listtask = []
    for task in tasks:
        if task.get('completed') is True:
            listtask.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(listtask), len(tasks)))
    for task in listtask:
        print("\t {}".format(task.get("title")))
