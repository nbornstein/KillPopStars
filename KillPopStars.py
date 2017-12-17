#!/usr/bin/python

from twitter import *
import sys

# parameter 1 is the ID of the tweet to start with
tweet_id = sys.argv[1]

# read the Twitter API auth from 'config' file
auth = {}
f = open('config')
for line in f:
    params = line.split()
    auth[params[0]] = params[1]

# log in to twitter
t = Twitter(auth=OAuth(auth['consumer_key'], auth['consumer_secret'], auth['access_token_key'], auth['access_token_secret']))

# get the base tweet
tweet = t.statuses.show(id=tweet_id)

# block the user
print 'Blocking original tweeter @'  + tweet['user']['screen_name'] + ' (' + tweet['user']['name'] + ')!'
t.blocks.create(screen_name=tweet['user']['screen_name'])

# get all retweets
retweets = t.statuses.retweets(id=tweet_id)

# block everyone who retweeted it
for retweet in retweets:
    print 'Blocking retweeter @'  + retweet['user']['screen_name'] + ' (' + retweet['user']['name'] + ')!'
    t.blocks.create(screen_name=retweet['user']['screen_name'])

