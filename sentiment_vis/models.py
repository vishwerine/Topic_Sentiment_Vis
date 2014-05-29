#! /usr/bin/env python

from django.db import models	

class SearchQuery(models.Model):
          query = models.CharField(max_length=30)

          def __unicode__(self):
                   return self.query


class TweetObject(models.Model):
         tweet = models.CharField(max_length=150) 
         query = models.CharField(max_length =30)
        
         def __unicode__(self):
                 return self.tweet



class EmotionObject(models.Model):
          tweet = models.ForeignKey('TweetObject')
          query = models.CharField(max_length=30)
          emotion = models.IntegerField()
          sentiment = models.BooleanField()


