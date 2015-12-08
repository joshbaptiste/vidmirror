import json
import sqlite
import redis
import requests
from myauth import client_id, client_secret, access_token, MY_USER_ID
from instagram.client import InstagramAPI

USER_ID_URL = 'http://jelled.com/ajax/instagram?do=username&username={}&format=json'
api = InstagramAPI(access_token=access_token, client_secret=client_secret)

class VidMirror():
    def get_user_id(self, username):
        try:
           r = requests.get(USER_ID_URL.format(username))
           output = r.json()
        except:
            pass

    def get_followed_users(self, user_id):
        return api.user_follows(user_id)

    def get():
        pass

if __name__ == '__main__':
    tvids = VidMirror()
    followed_users = tvids.get_followed_users(MY_USER_ID)
    for followed_user in followed_users:
        print followed_user
