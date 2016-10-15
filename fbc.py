# -*- coding: utf-8 -*-
__author__ = 'Shane_Kao'

import requests
import facebook

def get_short_lived_token(app_id, app_key):
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_key}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    result = file.text.split("=")[1]
    return result

token = get_short_lived_token('XXXXXXXXX', 'XXXXXXXXXX')

def get_facebook_data(object_id, p_fields):
    args = p_fields
    graph = facebook.GraphAPI(access_token = token, version = '2.7')
    profile = graph.get_object(object_id, **args)
    return profile


result = get_facebook_data(u'asusclub.tw',
                           {'fields':'posts.limit(10){created_time,from,message,permalink_url}'})
print repr(result).decode('unicode-escape')