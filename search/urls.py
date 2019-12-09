from django.conf.urls import url
from django.contrib import admin
from .views import searchposts, SearchPageView
from django.urls import path

urlpatterns = [
     url(r'^$', searchposts, name='searchposts'),
     path('search/', SearchPageView.as_view(), name='search'),

]
