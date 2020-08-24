#!/usr/bin/python3
'''
    Python script that takes in a URL,
    sends a request to the URL and displays
    the value of the variable X-Request-Id
    in the response header
'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    html = requests.post(url, email)
    print(html.text)
