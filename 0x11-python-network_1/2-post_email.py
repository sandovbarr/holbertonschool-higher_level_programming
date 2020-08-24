#!/usr/bin/python3
'''
    Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the
    email as a parameter, and displays the body of
    the response (decoded in utf-8)
'''
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    data = parse.urlencode(values)'''needs to be encoded in a standard way'''
    data = data.encode('ascii') '''data should be bytes'''
    req = request.Request(url, data) '''make the POST request of data'''

    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
