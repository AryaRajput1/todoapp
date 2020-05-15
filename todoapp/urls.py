
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
  path('', views.home),
  path('notes/', views.index),
  path('home/', views.home),
  path('cross/<int:id>/', views.cross),
  path('uncross/<int:id>/', views.uncross),
  path('delete/<int:id>/', views.deletenotes),
  path('signup/', views.signup),
  path('search/', views.searchnote),
  path('login/', views.logins),
  path('logout/', views.logouts),
  path('deleteall/', views.deleteall),
  path('restoreall/', views.restoreall),
  path('permanentdeleteall/', views.permanentdeleteall),
  path('deleteitems/', views.deleteitems),
  path('restore/<int:id>/', views.restore),
  path('permanentdelete/<int:id>/', views.permanentdelete),
 
]
