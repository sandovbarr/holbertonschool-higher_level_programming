#!/usr/bin/python3
'''
    Write a Python script that takes your Github
    credentials (username and password) and uses
    the Github API to display your id

    The letter must be sent in the variable q
    If no argument is given, set q=""
    If the response body is properly JSON formatted and not empty,
    display the id and name like this: [<id>] <name>

    Otherwise:
    Display Not a valid JSON if the JSON is invalid
    Display No result if the JSON is empty
    You must use the package requests and sys
    You are not allowed to import packages other
    than requests and sys
'''
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ''
    req = requests.post(url, {'q': letter})

    try:
        json = req.json()
        if not json:
            print('No result')
        else:
            print('[{}] {}'.format(json['id'], json['name']))
    except ValueError:
        print('Not a valid JSON')
