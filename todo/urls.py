
from django.contrib import admin
from django.urls import path,include
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # buttons for my projects
    path('',views.mainnav),
    path('todo/', include('todoapp.urls')),
]
