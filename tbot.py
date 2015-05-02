
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys

# Set keys to variables
# You get the keys by going to the twitter account manager
# and creating a new app. You then have to set permissions to
# read and write and create a token. Once you have your keys
# copy them here.
CONSUMER_KEY = 'VvIdgQtsgD9fRySXqkPq1Yddp'
CONSUMER_SECRET = 'AOsU7WkWwKLVPaOmP8BZN56P0IbnyGCicCbWsGb9XZERGp8q5N'
ACCESS_KEY = '3087994289-QzMLdi2wS8aYudyNTrBkfwM6Kpb0wc6JU1r9yOT'
ACCESS_SECRET = 'gO0Zcey3eKvwUzeKAhA34tKUCsiSpo2mEqL94B7qVjROM'

# The arg stuff is confusing but basically it means you set the
# file that the tweets are coming from when you run the Python
# script. So running the script looks like this:
# $ python tbot.py tweets.txt
argfile = str(sys.argv[1])

# Connect to API with keys set above and Tweepy library
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Open tweets.txt and read it line by line
# into a big list
filename=open(argfile,'r')
f=filename.readlines()
filename.close()

# Go through the list (f) line by line
# First tweet the line, then wait 1200 seconds
for line in f:
    api.update_status(status=line)
    time.sleep(6500)


