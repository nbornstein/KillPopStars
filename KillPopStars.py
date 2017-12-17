#!/usr/bin/python

from twitter import *
import sys

# parameter 1 is the ID of the tweet to start with
tweet_id = sys.argv[1]

# paramter 2 is the action to take - default is to block, but you can also mute or report.
action = 'block'
if sys.argv.count > 2:
    action = sys.argv[2]

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

# take action on the user
if (action == 'block'):
    print 'Blocking original tweeter @'  + tweet['user']['screen_name'] + ' (' + tweet['user']['name'] + ')!'
    t.blocks.create(screen_name=tweet['user']['screen_name'])
elif (action == 'mute'):
    print 'Muting original tweeter @'  + tweet['user']['screen_name'] + ' (' + tweet['user']['name'] + ')!'
    t.mutes.users.create(screen_name=tweet['user']['screen_name'])
elif (action == 'report'):
    print 'Reporting original tweeter @'  + tweet['user']['screen_name'] + ' (' + tweet['user']['name'] + ')!'
    t.users.report_spam(screen_name=tweet['user']['screen_name'])
else:
    print 'No action for original tweeter @'  + tweet['user']['screen_name'] + ' (' + tweet['user']['name'] + ')!'

# get all retweets
retweets = t.statuses.retweets(id=tweet_id)

# take action on everyone who retweeted it
for retweet in retweets:
    if (action == 'block'):
        print 'Blocking retweeter @'  + retweet['user']['screen_name'] + ' (' + retweet['user']['name'] + ')!'
        t.blocks.create(screen_name=retweet['user']['screen_name'])
    elif (action == 'mute'):
        print 'Muting retweeter @'  + retweet['user']['screen_name'] + ' (' + retweet['user']['name'] + ')!'
        t.mutes.users.create(screen_name=retweet['user']['screen_name'])
    elif (action == 'report'):
        print 'Reporting retweeter @'  + retweet['user']['screen_name'] + ' (' + retweet['user']['name'] + ')!'
        t.users.report_spam(screen_name=retweet['user']['screen_name'])
    else:
        print 'No action for retweeter @'  + retweet['user']['screen_name'] + ' (' + retweet['user']['name'] + ')!'

