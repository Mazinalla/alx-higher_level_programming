#!/usr/bin/python3
"""

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
