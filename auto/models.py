from email import message
from tkinter import Widget
from django.db import models


class Customer(models.Model):
    Id= models.AutoField(primary_key=True)
    Name = models.CharField(max_length=122,blank=False)
    email = models.EmailField(max_length=100,blank=False)
    username = models.CharField(max_length=200,blank=False)
    Age = models.IntegerField(blank=True)
    City =models.CharField(max_length=120)
    
company = (
    ('bmw','BMW'),
    ('mercedes','Mercedes'),
    ('maruti','Maruti'),
    ('lamborghini','Lamborghini'),
    ('honda','Honda'),
    ('toyota','Toyota'),
    ('mahindra','Mahindra'),
    ('tata','Tata'),
    ('skoda','Skoda'),
)
    
toc= (
    ('coupe','Coupe'),
    ('hatchback','Hatchback'),
    ('sedan','Sedan'),
    ('suv','SUV'),
    ('sports','Sports'),
    ('supercar','Supercar'),
    ('van','VAN'),
)

engpower = [tuple([i,i]) for i in range(1,11)]

class car(models.Model):
    car_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False)
    company = models.CharField(max_length=20,choices=company,default='bmw')
    type= models.CharField(max_length=20,choices=toc,default='coupe')
    engine = models.IntegerField(choices=engpower)
    seat_capacity = models.IntegerField(choices=engpower)
    price = models.IntegerField(blank=False)
    image = models.ImageField(upload_to='images',blank=False)
    
class contact(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=100,blank=False)
    msg = models.TextField(max_length=200,blank=False)
    

    