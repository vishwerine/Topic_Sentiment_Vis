from django.http import HttpResponse

import datetime
from src.twitter_handler import search_action, api_action


from django.template.loader import get_template
from django.template import Context


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)



def tweets(request):
      api = api_action.get_api()
      q = request.GET['q']
      s = search_action.search(q,api)

      return HttpResponse(s)



def index(request):
       t = get_template('search_form.html')
       html = t.render(Context({}))
       return HttpResponse(html)




