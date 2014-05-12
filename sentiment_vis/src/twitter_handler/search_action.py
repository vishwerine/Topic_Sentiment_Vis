#! /usr/bin/env python

### this file contains implementation for the search feature using the twitter's REST api


import tweepy

def search(q,api):
      ''' accesses the twitter's api to get tweets which match with the query q'''

      public_tweets = api.search(q)
   
      s = ""
      for tweet in public_tweets:
               s = s + "<p>" + tweet.text + "</p>"

      return s


       
