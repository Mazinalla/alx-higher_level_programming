#!/usr/bin/python3
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')
    print("Body response:")
    print("\t- type:", type(response.read()))
    print("\t- content:", response.read())
    print("\t- utf8 content:", body)
