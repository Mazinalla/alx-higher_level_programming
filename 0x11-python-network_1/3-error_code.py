#!/usr/bin/python3
"""

"""
import urllib.requests
import sys

url = sys.argv[1]

try:
    with requests.urlopen(url) as resp:
    body = resp.read()

    print(body)
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
