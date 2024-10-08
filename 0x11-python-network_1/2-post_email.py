#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(body)
