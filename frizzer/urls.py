from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('click',views.click,name='click'),
    path('show',views.show,name='show'),
    path('info',views.info,name='info'),
]