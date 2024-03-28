from django.db import models

class reg(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    psw=models.CharField(max_length=30)
    phone=models.IntegerField()
    ward=models.CharField(max_length=30)


class coordinate(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    password1=models.CharField(max_length=30)
    password2=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)

class member(models.Model):
    name=models.CharField(max_length=30)
    age=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    email=models.EmailField()
    ward=models.CharField(max_length=30)
    phone=models.IntegerField()
    password=models.CharField(max_length=30)

class Assign(models.Model):
    name=models.CharField(max_length=10)
    ward=models.CharField(max_length=10)
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

class update(models.Model):
    # fname=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    date=models.DateField()
    time=models.TimeField()
    area=models.CharField(max_length=30)
    description=models.CharField(max_length=30)

class pay(models.Model):
    name=models.CharField(max_length=30)
    # phonenumber=models.CharField(max_length=30)yth
    membername=models.CharField(max_length=30)
    price=models.CharField(max_length=30)


