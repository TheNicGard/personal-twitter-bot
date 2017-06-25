#!/usr/bin/python3
import config
import datetime
from random import randint
import threading
from threading import Timer
import tweepy

rate = 60.0 * 60.0 * 24 # determines how often bot tweets, in seconds
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

with open('adjectives.txt') as f:
    adjectives = f.readlines()
adjectives = [line.strip() for line in open('adjectives.txt')]

def generic_tweet(text):
    api.update_status(text[:140])

def interval_func():
    generic_tweet(bot_tweet())
    print("Tweeted at " + datetime.datetime.now().isoformat())
    Timer(rate, interval_func).start()

def bot_tweet():
    tweet = ""       
    while True:
        current_time = datetime.datetime.now().hour

        if current_time < 12:
            tweet = "Good morning!\nToday's gonna be "
        elif current_time >= 19:
            tweet = "Good morning.\nToday was "
        else:
            tweet = "Good morning.\nToday is "
        
        tweet += adjectives[randint(0, len(adjectives) - 1)]
        tweet += ".\n"
        tweet += str(randint(0, 9)) + "-" + "%02d" % randint(0, 99) + "-" + "%03d" % randint(0, 999)
        tweet += "\n#bot"

        if len(tweet) <= 140:
            break
    return tweet

interval_func()
