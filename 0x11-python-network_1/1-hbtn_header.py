#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import urllib.request
import sys

# Get the URL from command-line arguments
if __name__ == "__main__":
    url = sys.argv[1]

# Send a request to the URL
with urllib.request.urlopen(url) as response:
    # Get the value of the "X-Request-Id" variable from the response headers
    x_request_id = response.getheader('X-Request-Id')
    
    # Display the value of the "X-Request-Id" variable
    print(x_request_id)
