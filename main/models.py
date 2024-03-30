from django.db import models
from django.contrib.auth.models import User

class reg(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    email=models.CharField(max_length=30)
    psw=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()


class coordinate(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    password1=models.CharField(max_length=30)
    password2=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)


class Assign(models.Model):
    name=models.CharField(max_length=10)
    price=models.CharField(max_length=30)
    date=models.DateField()
    time=models.TimeField()
    area=models.CharField(max_length=30)
    description=models.CharField(max_length=30)

class feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()

class ufeedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()

class booking(models.Model):
    # fname=models.CharField(max_length=30)
    owner=models.ForeignKey(reg,on_delete=models.CASCADE, related_name='bookings')
    scrap_name=models.CharField(max_length=30)
    scrap_quantity=models.IntegerField()
    date=models.DateField()
    location=models.CharField(max_length=30)
    description=models.CharField(max_length=30)

class pay(models.Model):
    name=models.CharField(max_length=30)
    # phonenumber=models.CharField(max_length=30)yth
    membername=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
