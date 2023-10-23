#!/usr/bin/python3

"""Gather data from an API"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":

    user_url = 'https://jsonplaceholder.typicode.com/users'

    res = get(user_url)
    data = res.text
    data = json.loads(data)

    builder = {}

    for user in data:
        user_id = user.get('id')
        user_name = user.get('username')
        dictt = str(user_id)

        builder[dictt] = []

        task_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
            .format(user_id)
        res1 = get(task_url)

        data1 = res1.text

        data1 = json.loads(data1)

        for task in data1:
            json_data = {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_name
            }
            builder[dictt].append(json_data)
    # write the data to the file
    json_encoded_data = json.dumps(builder)
    with open('todo_all_employees.json', 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
