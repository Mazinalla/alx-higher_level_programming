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

# Get the URL and email from command-line arguments
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

# Encode the email parameter
data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')  # Encode the data to bytes

# Send a POST request to the URL with the email as a parameter
with urllib.request.urlopen(url, data) as response:
    # Read and decode the body of the response
    body = response.read().decode('utf-8')
    
    # Display the body of the response
    print(body)
