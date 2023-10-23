#!/usr/bin/python3

"""Gather data from an API"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    task_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(user_id)

    res = get(user_url)
    data = res.text
    data = json.loads(data)

    name = data.get('name')

    res1 = get(task_url)
    data1 = res1.text
    data1 = json.loads(data1)

    completed = 0
    tsk_len = len(data1)

    com_tasks = []

    for task in data1:
        if task.get('completed'):
            com_tasks.append(task)
            completed += 1

    builder = ""
    for task in data1:
        builder += '"{}","{}","{}","{}"\n'.format(
            user_id,
            name,
            task['completed'],
            task['title']
        )
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(builder)
