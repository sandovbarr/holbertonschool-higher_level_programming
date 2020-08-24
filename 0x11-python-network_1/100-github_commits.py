#!/usr/bin/python3
'''
    Python script that takes 2 arguments
    in order to solve this challenge.

    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
    You are not allowed to import packages
    other than requests and sys
'''
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'\
          .format(owner, repo)
    req = requests.get(url)
    json = req.json()
    counter = 0
    for el in json:
        print("{}: {}".format(el['sha'], el['commit']['author']['name']))
        counter += 1
        if counter == 10:
            break
