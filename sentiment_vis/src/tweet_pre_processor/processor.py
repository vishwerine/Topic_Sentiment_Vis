#! /usr/bin/env python

### does pre-processing on tweets to be used for lexicon matching

import re


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


def processing(list1):
      ''' this does simple regular expressions based processing '''
      list2 = []
      for tweet in list1:
        #Convert to lower case
        tweet = tweet.lower()
        #Convert www.* or https?://* to URL
        tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
        #Convert @username to AT_USER
        tweet = re.sub('@[^\s]+','AT_USER',tweet)
        #Remove additional white spaces
        tweet = re.sub('[\s]+', ' ', tweet)
        #Replace #word with word
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        #trim
        tweet = tweet.strip('\'"')
        list2.append(tweet)
        #end
      return list2



def pre_process(q):
         list1 = FetchTweets(q)
         
         list2 = processing(list1)

         return list2

