# -*- coding:utf-8 -*-
__author__ = 'wendong'

def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "https:127.0.0.1:8000/complete/weibo/"
    auth_url = weibo_auth_url + "?client_id={client_id}&redirect_url={re_url}".format(client_id=237999617, re_url=redirect_url)

    print(auth_url)

def get_access_token(code=''):
    access_token_url = 'https://api.weibo.com/oauth2/access_token'
    import requests
    re_dict = requests.post(access_token_url, data={
        "client_id": "",
        "client_secret": "",
        "grant_type": "authorization_code",
        "code": code,
        "redict_url": "https:127.0.0.1:8000/complete/weibo/"
    })


def get_user_info(access_token='', uid=''):
    user_url = ''
    print(user_url)


if __name__ == '__main__':
    get_auth_url()
    get_access_token(code='')
    get_user_info(access_token='', uid='')