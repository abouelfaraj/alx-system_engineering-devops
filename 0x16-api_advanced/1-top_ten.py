#!/usr/bin/python3
"""Module provide count of subscribers"""
import configparser
import requests


def top_ten(subreddit):
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

    params = {
            'limit': 10
            }

    auth = (client_id, client_secret)
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'AdvanceAPI-1.0.0'}
    response = requests.get(url=url,
                            data=data,
                            params=params,
                            auth=auth,
                            headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children_posts = data['data']['children']
        if len(children_posts) == 0:
            print(None)
        else:
            for post in children_posts:
                print(post['data']['title'])
    else:
        print(None)
        return 0
