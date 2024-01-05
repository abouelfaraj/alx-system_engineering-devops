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
    name = str(json_res.get('name'))

    todos = '{}todos?userId={}'.format(url, userid)
    res_todos = requests.get(todos)
    tasks = res_todos.json()
    listtask = []
    nbrtasks = 0
    alltasks = 0
    for task in tasks:
        if task.get('completed') is True:
            listtask.append(task)
            nbrtasks += 1
        alltasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, nbrtasks, alltasks))
    for task in listtask:
        print("\t {}".format(task.get("title")))
