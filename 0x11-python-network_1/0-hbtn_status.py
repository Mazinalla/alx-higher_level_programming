#!/usr/bin/python3
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    content = response.read()
    body = content.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", body)
