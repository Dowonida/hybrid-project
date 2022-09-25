from django.contrib import admin
from django.urls import path
from . import views
app_name='movies'
urlpatterns = [
     path('',views.main,name='main'),
     path('info/<title>',views.info,name='info'),
     path('search/',views.searching,name='search'),
     
     

]
