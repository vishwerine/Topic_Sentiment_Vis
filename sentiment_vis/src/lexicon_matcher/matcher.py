#! /usr/env/bin python


## source code for matching emotions and sentiments from the lexicon matcher

from sentiment_vis.models import TweetObject, EmotionObject

import string
import re

def FetchTweets(q):
       ''' internal function for retrieving tweets from database ''' 
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


class LexiconTweet:
         tweet = ""
         emotion = []


def match(q):
     ''' fetches data from database, stores emotions as well as sentiments in database '''
     
     list1 = FetchTweets(q)
     list2 = processing(list1)

     f = open('sentiment_vis/src/lexicon_matcher/nrc_emotion_lexicon.txt','r')
     line = f.readline()
     lexicon = []
     while line!= "":
            s = string.split(line)
            a = []
            a.append(s[0])
            a.append(s[1])
            a.append(s[2])
            lexicon.append(a)
            line = f.readline()
     
     ans = []
     
     for li in list2:
           obj0 = LexiconTweet()
           obj0.emotion = [] 
           words = string.split(li)
           
           for word in words:
                 for lex in lexicon:
                      if lex[0] == word:
                        if lex[2]=='1':
                            ## word found
                            obj0.emotion.append(lex[1]) 
                            break
           
           obj0.tweet = li
           ans.append(obj0)
           
     return ans                  
                   

       
     return ans
 
                  
                  

            
         

