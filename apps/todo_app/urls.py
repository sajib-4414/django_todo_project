from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.get_index_page, name='index'),
]
