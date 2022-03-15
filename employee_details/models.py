from django.db import models

# Create your models here.

class Region(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Employee(models.Model):
    companyname = models.CharField(max_length=100)
    business_reg_no = models.CharField(max_length=5)
    Email = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    region_based_in = models.ForeignKey(Region,on_delete=models.CASCADE)
    
