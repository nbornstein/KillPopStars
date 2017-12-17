#!/usr/bin/python

from twitter import *
import sys

# take the appropriate action on the user
def takeAction(api, a, u):
    if (a == 'block'):
        blockUser(api,u)
    elif (a == 'mute'):
        muteUser(api,u)
    elif (a == 'report'):
        reportUser(api,u)
    else:
        noActionUser(api,u)
        

# block the user
def blockUser(api, u):
    print 'Blocking @'  + u['screen_name'] + ' (' + u['name'] + ')!'
    api.blocks.create(screen_name=u['screen_name'])

# mute the user
def muteUser(api, u):
    print 'Muting @'  + u['screen_name'] + ' (' + u['name'] + ')!'
    api.mutes.users.create(screen_name=u['screen_name'])

# report the user
def reportUser(api, u):
    print 'Reporting @'  + u['screen_name'] + ' (' + u['name'] + ')!'
    api.users.report_spam(screen_name=u['screen_name'])

# take no action on the user
def noActionUser(api, u):
    print 'No action for @'  + u['screen_name'] + ' (' + u['name'] + ')!'


# main method
if __name__ == "__main__":

    # check usage
    if len(sys.argv) < 2:
        print
        print 'USAGE: ' + sys.argv[0] + ' <tweet_id> <action>'
        print
        print 'tweet_id is the Twitter ID of the tweet to start with'
        print 'action is the action to take: block (default), mute, or report'
        print
        print 'Requires a file in the current directory called \'config\' that has authorization parameters. The file should have this format:'
        print
        print 'consumer_key         <your_consumer_key>'
        print 'consumer_secret      <your_consumer_secret>'
        print 'access_token_key     <your_access_token_key>'
        print 'access_token_secret  <your_access_token_secret>'
        exit()

    # parameter 1 is the ID of the tweet to start with
    tweet_id = sys.argv[1]

    # parameter 2 is the action to take - default is to block, but you can also mute or report.
    action = 'block'
    if len(sys.argv) > 2:
        action = sys.argv[2]

    # read the Twitter API auth from 'config' file
    auth = {}
    f = open('config')
    for line in f:
        params = line.split()
        auth[params[0]] = params[1]

    # log in to twitter
    api = Twitter(auth=OAuth(auth['consumer_key'], auth['consumer_secret'], auth['access_token_key'], auth['access_token_secret']))

    # get the base tweet
    tweet = api.statuses.show(id=tweet_id)

    # take action on the user
    takeAction(api,action,tweet['user'])

    # get all retweets
    retweets = api.statuses.retweets(id=tweet_id)

    # take action on everyone who retweeted it
    for retweet in retweets:
        takeAction(api,action,retweet['user'])

    # get all likes

    # take action on everyone who liked it

    # alas, there is no API for likes :(