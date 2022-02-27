#Urls for subscribers app
from . import views
from django.urls import path

urlpatterns = [
    path('signup', views.SubscribeForm, name='sub_new'),
    ]