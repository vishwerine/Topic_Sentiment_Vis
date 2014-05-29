#! /usr/bin/env python

### this file contains implementation for the search feature using the twitter's REST api


import tweepy

from sentiment_vis.models import TweetObject




def FetchTweets(q):
       ''' internal function for retrieving tweets from database''' 
       list1 = TweetObject.objects.filter(query=q)
       if len(list1) < 100:
          list2 = []
          for li in list1:
            list2.append(li.tweet)
          list2.reverse()
          return list2
       else:
         leng = len(list1)
         for i in range(leng-100):
                 list1[i].delete()
         list2 = []
         for li in list1:
            list2.append(li.tweet)
         list2.reverse()
         return list2


def search(q,api):
      ''' accesses the twitter's api to get tweets which match with the query q'''

      public_tweets = api.search(q)
   
      ## putting a filter for tweets in english language only
     
      for t in public_tweets:
                if t.lang == "en":
                       # saving latest tweets to database
                       p1 = TweetObject(query=q , tweet=t.text )
                       p1.save()  
      # most recent tweets from the database will be fetched
      return FetchTweets(q)                   

   



