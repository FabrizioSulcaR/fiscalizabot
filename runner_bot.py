from fiscalizabot import TweetBot
import time
import json
import tweepy

API_KEY = '9ibaF7QN1evE7D9iiKEuzjkd0'
API_SECRET_KEY = 'fErUQSutaiFFT5beLZdO5cPMtRK54z1ui8nZupA1ZGi3HGYrcr'
ACCESS_TOKEN = '1449425397259673602-si8G3IJMzE3Lo3sCQblK57O0OzigGc'
ACCESS_SECRET_TOKEN = 'pfzM0kqnV1oEM4OEhkCQ9y4A1Gb9TbmkmdLzL6B0aQCpv'

auth= tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)

inicio = time.time()
x = TweetBot()
y = x.read_info()
z = x.read_i()

def compute():
    if len(y) == int(z[0]):
        pass
    else:
        for i in range(len(y) - int((z)[0])):
            x.post(y,i)
            x.upgrade_i(x.read_i())
            time.sleep(1)
        final = time.time()

compute()
