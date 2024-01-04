#!/usr/bin/python3
"""script to export data in the CSV format."""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users'.format(url)
    res = requests.get(user)
    json_res = res.json()
    list_json = {}
    for user in json_res:
        name = user.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(url, userid)
        res = requests.get(todos)
        tasks = res.json()
        list_to_json = []
        for task in tasks:
            list_dic = {
                        "username": name,
                        "task": task.get("title"),
                        "completed": task.get("completed")}
            list_to_json.append(list_dic)

        list_json[str(userid)] = list_to_json
    csv_filename = "todo_all_employees.json"
    with open(csv_filename, mode='w') as f:
        json.dump(list_json, f)
