#Henry Johnson
#this program will scrape tweets from users, and put those tweets into a txt file
#date created:11/27/20
#last edited: 12/6/20
import sys,tweepy
import private
import datetime, time

#authentication function
def twitter_aut():
    try:
        consumer_key = 'vkodkyVsnKwjp0W9WT5cLeLcx'
        consumer_secret = 'vDte4bVOP9Y06vtojPYUpZuMPv19xgOTrW1rx1rOZz70CisXP7'
        access_token = '1297934794588737542-Bjnt2loRJm9ynT2x3V02ZEv6Fvxdcz'
        access_secret = '2o7el1sqPXL1TIDkUaPXaTFGeiZ7ZI7ZQ7II2junGO4NW'
    except KeyError():
        sys.stderr.write("Twitter enviroment variable not set"+"\n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth
#*******************************************************************************


def get_twitter_client():
    auth = twitter_aut()
    client = tweepy.API(auth, wait_on_reate_limit = True)
    return client


if __name__ == '__main__':
    user = input('Enter username: ')
    client = get_twitter_client()
    for status in tweepy.Cursor(client.home_timeline, screen_name=user).items():
        print(status.text)