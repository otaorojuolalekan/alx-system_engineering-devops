#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
         v1.0.0 (by /u/olalekan_otaoroju)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(
        url, headers=headers, params=params,
        allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(child.get("data").get("title"))
     for child in results.get("children")]
