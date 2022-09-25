from django.contrib import admin
from django.urls import path
from . import views
app_name='articles'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('write/',views.write,name='write'),
    path('<int:pk>/',views.detail,name='detail'),#이름도 맞춰줘야한다.
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/update/',views.update,name='update'),
    
]
