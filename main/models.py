from django.db import models
from django.contrib.auth.models import User

class reg(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    email=models.CharField(max_length=30)
    psw=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()

class feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()

class ufeedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()

from django.utils import timezone

class booking(models.Model):
    owner = models.ForeignKey(reg, on_delete=models.CASCADE, related_name='bookings')
    scrap_name = models.CharField(max_length=30)
    scrap_quantity = models.IntegerField()
    date = models.DateField()
    location = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status_choices = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    timestamp = models.DateTimeField(default=timezone.now)  # Field for booking creation date and time
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Add total_price field

    def __str__(self):
        return f"{self.owner.username}'s booking for {self.scrap_name} on {self.date}"



class pay(models.Model):
    name=models.CharField(max_length=30)
    # phonenumber=models.CharField(max_length=30)yth
    membername=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
