#!/usr/bin/python3

"""
script that takes in a url to send a request to the url
and display the values of the variable X-Request-Id

"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    info = response.headers
    print(info.get('x-request-id'))
