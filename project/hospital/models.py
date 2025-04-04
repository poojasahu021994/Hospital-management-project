from django.db import models

class EmployeeData(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_email=models.EmailField()
    emp_DOJ=models.DateField()
    emp_dep=models.CharField(max_length=50)
    emp_contact=models.IntegerField()
    emp_password=models.CharField(max_length=50)
    emp_work=models.CharField(max_length=100)
    
# Create your models here.
