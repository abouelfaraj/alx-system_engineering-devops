#!/usr/bin/python3
"""Module provide count of subscribers"""
import configparser
import requests


def number_of_subscribers(subreddit):
    """Get count of subscribers"""
    config = configparser.ConfigParser()
    config.read('config.txt')
    client_id = config.get('RedditAuth', 'client_id')
    client_secret = config.get('RedditAuth', 'client_secret')
    username = config.get('RedditAuth', 'username')
    password = config.get('RedditAuth', 'password')
    data = {
            'grant_type': 'password',
            'username': username,
            'password': password,
            }
    auth = (client_id, client_secret)
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'AdvanceAPI-1.0.0'}
    response = requests.get(url=url,
                            data=data,
                            auth=auth,
                            headers=headers,
                            allow_redirects=False)
    if response.status_code != 200:
        return 0
    if 'data' not in response.json():
        return 0
    if 'subscribers' not in response.json()['data']:
        return 0
    return response.json()['data']['subscribers']
