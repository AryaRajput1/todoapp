from django.contrib import admin
from todoapp.models import Notes,Userdata
# Register your models here.
admin.site.site_header='Arya Rajput'
admin.site.register(Notes)
admin.site.register(Userdata)