#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

# Get the URL and email from command-line arguments
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
