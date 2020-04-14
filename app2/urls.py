from django.contrib import admin
from django.urls import path
import app2.views


#from .import views

urlpatterns = [
    path('etc/', app2.views.etc, name= "etc")
]
