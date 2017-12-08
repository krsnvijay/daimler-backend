from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', login),
    url(r'^select\.html/', select),
    url(r'^manifest\.json/', manifest),
    # url(r'^$', home),
    # url(r'^$', home),
    # url(r'^$', home),
]