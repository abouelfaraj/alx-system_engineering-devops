#!/usr/bin/python3
"""script that returns information about an employee TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_res = res.json()
    print("Employee {} is done with tasks".format(
        json_res.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    listtask = []
    for task in tasks:
        if task.get('completed') is True:
            listtask.append(task)

    print("({}/{}):".format(len(listtask), len(tasks)))
    for task in listtask:
        print("\t{}".format(task.get("title")))
