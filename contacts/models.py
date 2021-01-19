from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Contact_sodesh(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    plot_number  = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.username
# NewDhakaCity part

class Contact_NewDhakaCity(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    plot_number  = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.username

#part Swadesh
class Contact_Swadesh(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    plot_number  = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.username
#part RiverParkModelTown
class Contact_RiverParkModelTown(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    plot_number  = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.username




class Contact_from_compnay(models.Model):
    username = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    package_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    def __str__(self):
        return self.company_name