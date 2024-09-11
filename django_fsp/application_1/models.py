from django.db import models

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    message=models.CharField(max_length=255)

class Product(models.Model):
    name=models.CharField(max_length=122)
    description=models.CharField(max_length=122)
    price=models.DecimalField(max_digits=5,decimal_places=2)