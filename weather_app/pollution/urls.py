from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'addCity/$',views.addCity,name="addCity"),
    path('',views.home,name='home'),
    path('fromList/<int:slug>',views.from_list,name='fromList'),
    path('delete/<int:slug>',views.delete,name='delete'),
    
    url(r'currentCity/$',views.currentCity,name="currentCity"),

]