from django.db import models

# Create your models here.
class student(models.Model):
        name=models.CharField(max_length=10)
        age=models.IntegerField()
        place=models.CharField(max_length=10)
        dob=models.DateField()
class products(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=10)
    desc=models.TextField(max_length=100)
    price=models.IntegerField()
    
    def __str__(self):
      return self.name

class signup(models.Model):
        username=models.CharField(max_length=10)
        email=models.EmailField(max_length=30)
        password=models.CharField(max_length=20)
class register(models.Model):
        name=models.CharField(max_length=10)
        username=models.CharField(max_length=10)
        password=models.CharField(max_length=20)
        email=models.EmailField(max_length=30)
class new(models.Model):
        name=models.CharField(max_length=100)
        document=models.CharField(max_length=100)
        
        
