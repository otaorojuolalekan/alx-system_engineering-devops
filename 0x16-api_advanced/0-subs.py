#!/usr/bin/python3
"""
Contains the function for number_of_subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    resp = requests.get(
        'http://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={'User-Agent': '0x16-api_advanced:project:\
        v1.0.0 (by /u/olalekan_otaoroju)'}).json()
    count_subs = resp.get("data", {}).get("subscribers", 0)
    return count_subs
