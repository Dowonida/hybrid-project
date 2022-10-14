from django.contrib import admin
from django.urls import path
from . import views
app_name='movies'
urlpatterns = [
     path('',views.index,name='index'),
     path('create/', views.create, name='create'),
     path('<int:movie_pk>/update/', views.update, name='update'),
     path('<int:movie_pk>', views.detail, name='detail'),
     path('<int:movie_pk>/delete',views.delete, name='delete'),
     path('info/<title>',views.info,name='info'),
     path('search/',views.searching,name='search'),
     path('<int:movie_pk>/comments/',views.comments,name='comments'),
     path('<int:movie_pk>/comments/<comment_pk>/delete/',views.comments_delete,name='comments_delete'),
     

]
