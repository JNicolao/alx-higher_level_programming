#!/usr/bin/python3

"""
script that fetches https://alx-intranet.hbtn.io/status

"""


from requests import get


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = get(url)
    bytes_content = response.text
    string = 'Body response:\n\t- type: {}\n\t- content: {}'.format(
             type(bytes_content), bytes_content)
    print(string)
