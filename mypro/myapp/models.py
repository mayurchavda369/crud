from django.db import models

# Create your models here.
class User(models.Model):

    firstname=models.CharField(max_length=60)
    lastname=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=10)
    mobile=models.IntegerField(default=0)
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=60)
    
    def __str__(self):
        return self.firstname
