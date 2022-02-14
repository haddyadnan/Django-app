#Urls for marketing app
from . import views
from django.urls import path
from django.views.generic import TemplateView

# urlpatterns = [
#     path('', views.HomePage, name='home'),

# ]
##Boiler plate
urlpatterns = [
    path('', TemplateView.as_view(template_name='marketing/home.html')),

]