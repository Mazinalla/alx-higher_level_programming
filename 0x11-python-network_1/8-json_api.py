#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        json_resp = response.json()

        if json_resp:
            print(f"[{json_resp.get('id')}] {json_resp.get('name')}")
        else:
            # If the JSON is empty, display "No result"
            print("No result")
    except ValueError:
        # If JSON decoding fails, display "Not a valid JSON"
        print("Not a valid JSON")
