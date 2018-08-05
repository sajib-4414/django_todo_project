from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.get_index_page, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.get_details_page,name='details'),
    url(r'^add/$', views.add_todo,name='add_todo')
]
