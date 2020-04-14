from django.contrib import admin
from django.urls import path
import app1.views
import app2.views

#from .import views

urlpatterns = [
    path('', app1.views.home, name= "home"),
    path('profile/', app1.views.profile, name= "profile"),
    path('hobby/', app1.views.hobby, name= "hobby"),
    path('etc/', app2.views.etc, name= "etc"),
    path('hobby/suin/',app1.views.suin,name="suin"),
    path('hobby/alcohol/',app1.views.alcohol,name="alcohol" )
]