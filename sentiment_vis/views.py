from django.http import HttpResponse

from src.twitter_handler import search_action, api_action


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
        list2 = ['hi','why','ty']
        
        return render(request,'display_tweets2.html',{'list1': list1})
      else:
        return HttpResponse("<p> Error: Search Query not specified. Go to Index and type in your query </p>")
      


def index(request):
       t = get_template('navbar_body.html')
       html = t.render(Context({}))
       return HttpResponse(html)




