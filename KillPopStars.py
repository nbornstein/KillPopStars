#!/usr/bin/python

from twitter import *
import sys
import urllib2
import re
import os


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

# get the user IDs of everyone who liked the original tweet 
# alas, there is no API for likes :(
# https://stackoverflow.com/questions/28982850/twitter-api-getting-list-of-users-who-favorited-a-status
# WARNING: this may be fragile as it depends on scraping HTML
def get_user_ids_of_post_likes(post_id):
    try:
        json_data = urllib2.urlopen('https://twitter.com/i/activity/favorited_popup?id=' + str(post_id)).read()
        found_ids = re.findall(r'data-user-id=\\"+\d+', json_data)
        unique_ids = list(set([re.findall(r'\d+', match)[0] for match in found_ids]))
        return unique_ids
    except urllib2.HTTPError:
        return False

# check usage
def checkUsage():
    # check usage
    if len(sys.argv) < 2:
        print
        print 'USAGE: ' + sys.argv[0] + ' <tweet_id> <action>'
        print
        print 'tweet_id is the Twitter ID of the tweet to start with'
        print 'action is the action to take: block (default), mute, or report'
        print
        print 'Requires a file called \'config\' that has authorization parameters, which will be read from the local directory, a .KillPopStars directory in the user\'s home directory, or the /etc/KillPopStars/ directory. The file should have this format:
'
        print
        print 'consumer_key         <your_consumer_key>'
        print 'consumer_secret      <your_consumer_secret>'
        print 'access_token_key     <your_access_token_key>'
        print 'access_token_secret  <your_access_token_secret>'
        exit()

# read the Twitter API auth from 'config' file
def getAuth():
    auth = {}
    
    # first look in local directory for a config file
    path = 'config'
    if not (os.path.exists(path)):
        path = os.path.expanduser('~') + '/.KillPopStars/config'
        if not (os.path.exists(path)):
            path = '/etc/killpopstars/config'
            if not (os.path.exists(path)):
                print("No config file found.")
                exit(2)

    print "Using config file from " + path
    f = open(path)
    for line in f:
        params = line.split()
        auth[params[0]] = params[1]
    
    return auth;


# main method
if __name__ == "__main__":

    # check usage
    checkUsage()

    # parameter 1 is the ID of the tweet to start with
    tweet_id = sys.argv[1]

    # parameter 2 is the action to take - default is to block, but you can also mute or report.
    action = 'block'
    if len(sys.argv) > 2:
        action = sys.argv[2]

    # read the Twitter API auth from 'config' file
    auth = getAuth()

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
    likes = get_user_ids_of_post_likes(tweet_id)

    # take action on everyone who liked it
    for like in likes:
        user = api.users.lookup(user_id=like)[0]
        takeAction(api,action,user)
