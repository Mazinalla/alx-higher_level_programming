#!/usr/bin/python3

"""
Python script that takes 2 arguments in order to solve this challenge.
- this is an interview challenge my boy.
"""

import requests
import sys


def list_commits(repo_name, owner_name):
    # GitHub API URL for the repository commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    # Request the most recent 10 commits
    response = requests.get(url, params={'per_page': 10})
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            # Extract and print the commit SHA and author name
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Failed to retr commits. Status code: {response.status_code}")


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    list_commits(repo_name, owner_name)
