#! /usr/env/python

### this returns the api object after OAuth credentials

import tweepy

def get_api():
      ''' returns the api interface to be used later'''
      
      #read_credentials = open('credentials.txt','r')
      
      #ck = read_credentials.readline()
      #if ck=="":
      #     print "Error: Consumer key not specified in credentials.txt"
      #cs = read_credentials.readline()
      #if cs=="":
      #     print "Error: Consumer key secret not specified in credentials.txt"
           
      #at = read_credentials.readline()
      #if at=="":
      #     print "Error: Auth token not specified in credentials.txt"
            
      #ats = read_credentials.readline()
      #if ats=="":
      #     print "Error: Auth token secret not specified in credentials.txt"

      auth = tweepy.OAuthHandler('Ohqs1xx5t6XOfm1Fm7qHeVfz2','zLWvNpBLPIbPhSyawX8PuN9wDkB8OEv1fLt8IlOmib7ZqwPkiQ')
      auth.set_access_token('2489682726-hOGLydWvgQn79GmXl0BmjnVCYGtmNmI5CFF7HEb','adQzxcB7S0EE3j62JCZRqf0l6Iu9VPdAONcnOf7IUrFRX')
      api = tweepy.API(auth)

      return api
    

     
      
