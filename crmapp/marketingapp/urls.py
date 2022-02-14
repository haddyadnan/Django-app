#Urls for marketing app
from . import views
from django.urls import path

urlpatterns = [
    path(r'^$', views.HomePage, name='home'),
    
]