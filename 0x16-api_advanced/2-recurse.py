#!/usr/bin/python3
"""Module provide count of subscribers"""
import configparser
import requests


def append_title(h_list, h_posts):
    """Append items to list """
    if len(h_posts) == 0:
        return
    h_list.append(h_posts[0]['data']['title'])
    h_posts.pop(0)
    append_title(h_list, h_posts)


def recurse(subreddit, hot_list=[], after=None):
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
            'after': after
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
        h_posts = data['data']['children']
        append_title(hot_list, h_posts)
        after = data['data']['after']
        if not after:
            return hot_list
        return recurse(subreddit, hot_list=hot_list, after=after)
    else:
        return None
