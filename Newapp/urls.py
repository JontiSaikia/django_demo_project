from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from Newapp import views

urlpatterns = [
   path('favicon.ico',RedirectView.as_view(url='/static/images/favicon.ico')),
   path('',views.index,name='index'),
   path("about",views.about,name='about'),
   path("services",views.services,name='services'),
   path("contact",views.contact,name='contact'),
   path('loginUser',views.loginUser,name='loginUser'),
   path('logout',views.logoutUser,name="logoutUser")
   
]