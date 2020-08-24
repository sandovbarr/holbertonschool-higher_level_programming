#!/usr/bin/python3
'''
    Python script that takes your Github credentials
    (username and password) and uses the Github API to display your id

    You must use Basic Authentication with a personal access token as
    password to access to your information
    (only read:user permission is needed)

    The first argument will be your username
    The second argument will be your password
    (in your case, a personal access token as password)

    You must use the package requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)
'''
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'

    try:
        req = requests.get(url, auth=(username, token))
        json = req.json()
        if 'id' in json.keys():
            print('{}'.format(json['id']))
        else:
            print('None')
    except ValueError:
        print('Not a valid JSON')
