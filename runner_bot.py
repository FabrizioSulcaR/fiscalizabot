from fiscalizabot import TweetBot
from dotenv import load_dotenv
import time
import tweepy
import os


API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET_TOKEN = os.getenv('ACCESS_SECRET_TOKEN')

auth= tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)

inicio = time.time()
x = TweetBot()
y = x.read_info()
z = x.read_i()
intros = x.read_intros()

def compute():
    if len(y) == int(z[0]):
        pass
    else:
        for i in range(len(y) - int((z)[0])):
            x.post(y,int(z[0])+i, intros)
            x.upgrade_i(x.read_i())
            time.sleep(3)
        final = time.time()
        print(final-inicio)

load_dotenv()
compute()