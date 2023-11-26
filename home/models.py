from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=255, default='', null=False)
    phone_number = models.CharField(max_length=15, default='', null=False)
    address = models.CharField(max_length=255, default='', null=False)
    age = models.IntegerField(default=0, null=False)  
    pin_code = models.CharField(max_length=10, default='', null=False)

class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255)


class Service(models.Model):
    ServiceID = models.AutoField(primary_key=True)
    ServiceName = models.CharField(max_length=255)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE)


class Appointment(models.Model):
    AppointmentID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    ServiceID = models.ForeignKey(Service, on_delete=models.CASCADE)
    AppointmentDate = models.DateField()
    AppointmentTime = models.TimeField()

class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    Employee_name = models.CharField(max_length=255, default='', null=False)
    CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    ServiceID = models.ForeignKey(Service, on_delete=models.CASCADE)
    Date_of_birth = models.DateField()
    Phone_number = models.CharField(max_length=15, default='', null=False)
    Address = models.CharField(max_length=255, default='', null=False)
    Age = models.IntegerField(default=0, null=False)  
    Pin_code = models.CharField(max_length=10, default='', null=False)