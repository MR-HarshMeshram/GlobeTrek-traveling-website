from email.policy import default
from django.db import models

# Create your models here.
class package(models.Model):
    package_id=models.AutoField
    package_name=models.CharField(max_length=50)
    package_dis=models.CharField(max_length=50)
    package_image=models.ImageField(upload_to="traveling/image",default="")
    pub_date=models.DateField()
    
    def __str__(self):
        return self.package_name
    
class Destinations(models.Model):
    destinations_id=models.AutoField
    destinations_name=models.CharField(max_length=50)
    destinations_dis=models.CharField(max_length=50)
    destinations_image=models.ImageField(upload_to="traveling/image",default="")
    destinations_date=models.DateField()
    
    def __str__(self):
        return self.destinations_name
 
class Book(models.Model):
        msg_id=models.AutoField(primary_key=True)
        name =models.CharField(max_length=50)
        email =models.CharField(max_length=50)
        phone =models.CharField(max_length=50)
        address =models.CharField(max_length=50)
        location =models.CharField(max_length=50)
        arrivals=models.CharField(max_length=50) 
        leaving=models.CharField(max_length=50) 
        guests =models.CharField(max_length=50)

        def __str__(self):
           return self.name