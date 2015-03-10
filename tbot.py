#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys

CONSUMER_KEY = 'mNSas1jm4pczVaPRN9i1BL4eD'
CONSUMER_SECRET = 'SENlVoUvk0DZQZGLhLa0xhxOANcrUnmARlgH4w6D9KJ45JSCmV'
ACCESS_KEY = '2490481441-qX1WKAC80J0rMhyjmSlBsoEfWPHkweagOgLvxRH'
ACCESS_SECRET = 'CsZI9AkdnWFspqfmZmS0IZBnj1NIbklFjCvffPurbv6Qt'

argfile = str(sys.argv[1])

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(status=line)
    time.sleep(9000)


