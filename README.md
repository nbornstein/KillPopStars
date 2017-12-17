# KillPopStars

A handy script to block the author of a tweet and everyone who retweets or likes that tweet.

I created this script because my Twitter handle ([@niel](http://twitter/comn/niel)) is constantly being mistaken for someone else. (If you must know, French businessman [Xavier Niel](https://twitter.com/xavier75), the town of [Niel](http://twitter.com/gemeenteniel) in Belgium, Filipino pop star [Niel Murillo](https://en.wikipedia.org/wiki/BoybandPH), and K-Pop boy band star [Ahn Daniel](https://en.wikipedia.org/wiki/Niel_(singer)). The last two are the most annoying as they don't have verified Twitter accounts and seem to have millions of fans who like to retweet each other.) So when I get a tweet intended for one of these people, I just want it to go away as quickly and efficiently as possible.

I wrote this script to block these users for my own purpose, but it could also easily be used to mute them or report spammers if, for example, you are being harassed on Twitter.

## Usage

```
KillPopStars.py <tweet_id> <action>
```

*tweet_id* is the Twitter ID of the tweet to start with

*action* is the action to take: block (default), mute, or report

Requires a file in the current directory called 'config' that has authorization parameters. The file should have this format:

```
consumer_key        <your_consumer_key>
consumer_secret     <your_consumer_secret>
access_token_key    <your_access_token_key>
access_token_secret <your_access_token_secret>
```

Get your own keys at https://apps.twitter.com/.