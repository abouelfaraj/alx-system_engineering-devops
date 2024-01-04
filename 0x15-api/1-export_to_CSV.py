#!/usr/bin/python3
"""script to export data in the CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_res = res.json()

    todos = '{}todos?user={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    list_to_csv = []
    for task in tasks:
        list_to_csv.append([
            json_res.get("id"), 
            json_res.get("username"), 
            task.get("completed"), 
            task.get("title")
            ])
    csv_filename = "{}.csv".format(json_res.get("id"))
    with open(csv_filename, mode='w') as employee:
        employee_w = csv.writer(
                employee,delimiter=',',
                quotechar='"',
                quoting=csv.QUOTE_ALL)
        for task in list_to_csv:
            employee_w.writerow(task)

