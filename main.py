#Henry Johnson
#This program recieves tweets using the tweepy api
#created: 11/5/20
#edited: 12/15/20
import json
import tweepy

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("vkodkyVsnKwjp0W9WT5cLeLcx", "vDte4bVOP9Y06vtojPYUpZuMPv19xgOTrW1rx1rOZz70CisXP7")
auth.set_access_token("1297934794588737542-Bjnt2loRJm9ynT2x3V02ZEv6Fvxdcz", "2o7el1sqPXL1TIDkUaPXaTFGeiZ7ZI7ZQ7II2junGO4NW")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)


tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["proud boys", "vaccine", "Kan ye"],
              languages=["en"])