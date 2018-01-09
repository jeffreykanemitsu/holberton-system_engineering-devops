#!/usr/bin/python3
'''
Write a function that queries the Reddit API (https://www.reddit.com/dev/api/)
and returns the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given, the function
should return 0.
'''
import requests


def number_of_subscribers(subreddit):
    '''
    returns the numbrer of subscribers
    '''
    url = 'http://www.reddit.com/r/{:s}/about.json'.format(subreddit)
    headers = {'User-agent': 'Jeffrey'}
    r = requests.get(url, headers=headers)
    subs = r.json().get('data').get('subscribers')
    if subs is None:
        return 0
    else:
        return subs
