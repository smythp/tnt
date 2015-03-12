#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys

CONSUMER_KEY = 'VvIdgQtsgD9fRySXqkPq1Yddp'
CONSUMER_SECRET = 'AOsU7WkWwKLVPaOmP8BZN56P0IbnyGCicCbWsGb9XZERGp8q5N'
ACCESS_KEY = '3087994289-QzMLdi2wS8aYudyNTrBkfwM6Kpb0wc6JU1r9yOT'
ACCESS_SECRET = 'gO0Zcey3eKvwUzeKAhA34tKUCsiSpo2mEqL94B7qVjROM'

argfile = str(sys.argv[1])

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(status=line)
    time.sleep(6500)


