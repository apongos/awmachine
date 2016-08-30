from django.http import Http404
from django.shortcuts import render
from time import gmtime, strftime

def home(request):
  context = dict()
  context['current_time'] = strftime('%a, %d %b %Y %H:%M:%S', gmtime())
  return render(request, 'home/index.html', context)

