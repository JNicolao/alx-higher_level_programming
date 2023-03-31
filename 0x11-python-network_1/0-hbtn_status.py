#!/usr/bin/python3

"""
script that fetches https://alx-intranet.hbtn.io/status
"""

from urllib.request import urlopen


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        bytes_content = response.read()
        content = bytes_content.decode('utf-8')
        string = 'Body response:\n\t- type: {}\n\t- content: {}\n\t- \
utf8 content: {}'.format(type(bytes_content), bytes_content, content)
        print(string)
