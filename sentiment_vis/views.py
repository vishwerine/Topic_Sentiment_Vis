from django.http import HttpResponse

from src.twitter_handler import search_action, api_action
from src.tweet_pre_processor import processor
from src.lexicon_matcher import matcher

from django.template.loader import get_template
from django.template import Context


from django.shortcuts import render
from sentiment_vis.models import SearchQuery



def search_history(request):
    queries = SearchQuery.objects.all()
    
    return render(request,'search_list.html',{'queries' : queries})



def tweets(request):
      api = api_action.get_api()
      if 'q' in request.GET.keys():
        q = request.GET['q']
      
        p1 = SearchQuery(query=q)
        p1.save()
        list1 = search_action.search(q,api)
        
        return render(request,'tweets4.html',{'list1': list1, 'q' : q})
      else:
        return render(request,'error_no_query.html',{})
      


def index(request):
       t = get_template('index2.html')
       html = t.render(Context({}))
       return HttpResponse(html)


def update(request):
        q = request.GET['q']
        api = api_action.get_api()
        list1 = search_action.search(q,api)
        return render(request,'tweets4.html',{'list1':list1,'q':q})



def preProcess(request):
        q = request.GET['q']
        list1 = processor.pre_process(q)
        
        
        return render(request,'processed_tweets.html',{'list1':list1,'q':q})


def emotion(request):
       q = request.GET['q']
       ans = matcher.match(q)
       return render(request,'lexicon_tweets.html',{'ans':ans})

def topics(request):
       return render(request,'topics.html',{})

def sentiments(request):
       return render(request,'sentiments.html',{})


