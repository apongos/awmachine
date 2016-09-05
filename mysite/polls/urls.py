from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<comment_id>[0-9]+)/vote/$', views.vote, name='vote'),

    #Create comment polls/new
   	url(r'^new/$', views.StatementCreate.as_view(), name='comment-new'),
   	#Edit comment polls/2
   	url(r'^comment/(?P<pk>[0-9]+)/$', views.StatementUpdate.as_view(), name='comment-update'),
   	#Delete comment
   	url(r'^comment/(?P<pk>[0-9]+)/delete/$', views.StatementDelete.as_view(), name='comment-delete'),

   	#Create Counter Argument
   	url(r'^new/Counter-Argument/(?P<pk>[0-9]+)/$', views.CounterArgCreate.as_view(), name='counter-argument-new'),
]