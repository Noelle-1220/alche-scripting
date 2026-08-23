#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alche-api-advanced-qz84n:v1.0 (by /u/evika_dev)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
    except requests.exceptions.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json().get("data")
    except ValueError:
        print(None)
        return

    if data is None:
        print(None)
        return

    posts = data.get("children", [])
    if not posts:
        print(None)
        return

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
