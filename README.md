# KillPopStars

A handy script to block the author of a tweet and everyone who retweets that tweet.

I created this script because my Twitter handle (@niel) is constantly being mistaken for someone else. (If you must know, French businessman @xavier75, the town of @gemeenteniel in the Netherlands, K-Pop boy band star Daniell Ahn, and Filipino pop star Niel Murillo. The last two are the most annoying as they seem to have millions of fans who like to retweet each other.) So when I get a tweet intended for one of these people, I just want it to go away.

I wrote this script to block these users for my purpose. It could also easily be used to mute them or report spammers if, for example, you are being harassed on Twitter.

## Usage

```
KillPopStars.py <tweet_id> <action>
```

*tweet_id* is the Twitter ID of the tweet to start with

*action* is the action to take: block, mute, or report

Requires a file in the current directory called 'config' that has authorization paramenters.