#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import sys

url = sys.argv[1]
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(url) as resp:
            body = resp.read().decode('utf-8')

            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
