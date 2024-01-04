#!/usr/bin/python3
"""script to export data in the CSV format."""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_res = res.json()

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    list_to_json = []
    for task in tasks:
        list_dic = {"task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": json_res.get("username")}
        list_to_json.append(list_dic)
    str_list = {str(sys.argv[1]): list_to_json}
    csv_filename = "{}.json".format(sys.argv[1])
    with open(csv_filename, mode='w') as f:
        json.dump(str_list, f)
