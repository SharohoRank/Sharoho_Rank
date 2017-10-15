#coding:utf-8
import tweepy

CONSUMER_KEY = "xxx"
CONSUMER_SECRET = "xxx"
ACCESS_TOKEN = "xxx"
ACCESS_TOKEN_SECRET = "xxx"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
user=api.me().screen_name
follower = api.followers_ids(user)
friends = api.friends_ids(user)
set_apr = set(follower) - set(friends)
list_apr = list(set_apr)
for user in list_apr:
   try:
       api.create_friendship(user)
   except tweepy.error.TweepError:
       continue
