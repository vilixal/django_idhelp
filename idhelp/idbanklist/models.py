from django.db import models

# Create your models here.
class Idbanklist(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200,blank=True)
    status = models.CharField(max_length=20)
    mail = models.CharField(max_length=1000)
    dbms = models.CharField(max_length=10,blank=True)
    version = models.CharField(max_length=20,blank=True)
    is_public = models.BooleanField(default=True)
