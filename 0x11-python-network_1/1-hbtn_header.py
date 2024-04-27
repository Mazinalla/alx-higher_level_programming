import urllib.request
import sys

# Get the URL from command-line arguments
url = sys.argv[1]

# Send a request to the URL
with urllib.request.urlopen(url) as response:
    # Get the value of the "X-Request-Id" variable from the response headers
    x_request_id = response.getheader('X-Request-Id')
    
    # Display the value of the "X-Request-Id" variable
    print(x_request_id)
