#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url)
    x_request_id = resp.headers.get("X-Request-Id")
    # Print the value if the header exists, otherwise print a message
    if x_request_id is not None:
        print(x_request_id)
    else:
        print("X-Request-Id header not found")
