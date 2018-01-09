#!/usr/bin/python3
'''
Write a function that queries the Reddit API (https://www.reddit.com/dev/api/)
and prints the titles of the first 10 hot posts listed for a given subreddit.
'''
import requests


def top_ten(subreddit):
    '''
    returns top ten hot postss
    '''
    try:
        url = 'http://www.reddit.com/r/{:s}/hot.json?limit=10'
        .format(subreddit)
        headers = {'User-agent': 'Jeffrey'}
        r = requests.get(url, headers=headers)
        ten = r.json().get('data').get('children')
        for num in ten:
            print(num.get('data').get('title'))
    except:
        print(None)
