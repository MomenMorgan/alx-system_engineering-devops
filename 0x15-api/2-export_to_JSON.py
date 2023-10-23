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

    name = data.get('username')

    res1 = get(task_url)
    data1 = res1.text
    data1 = json.loads(data1)

    completed = 0
    tsk_len = len(data1)

    dictt = str(user_id)

    builder = {dictt: []}
    for task in data1:
        json_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": name
        }
        builder[dictt].append(json_data)
    json_encoded_data = json.dumps(builder)
    with open('{}.json'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
