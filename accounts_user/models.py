from django.db import models
from datetime import datetime

# Create your models here.
class SodeshOwnerUser(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    plot_no = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    paid_ammount = models.CharField(max_length=20)
    Total_ammount = models.CharField(max_length=20)
    update_date = models.DateField(default=datetime.now)
    first_installment = models.DateField()

class SodeshEmployee(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)

class SornaliOwnerUser(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    plot_no = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    paid_ammount = models.CharField(max_length=20)
    Total_ammount = models.CharField(max_length=20)
    update_date = models.DateField(default=datetime.now)
    first_installment = models.DateField()

class SornaliEmployee(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)