from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    note_id = models.AutoField(primary_key=True)
    note=models.CharField(max_length=1000,default='')
    date=models.DateField(auto_now_add=True)
    note_cross=models.BooleanField(default=False)
    note_saved=models.BooleanField(default=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    def __str__(self):
        m=self.note
        return m[:15]+'...'


class Userdata(models.Model):
  
    phone=models.CharField(max_length=10)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)