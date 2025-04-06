from django.db import models

class DoctorData(models.Model):
    doc_name=models.CharField(max_length=50)
    doc_email=models.EmailField()
    doc_DOJ=models.DateField()
    doc_dep=models.CharField(max_length=50)
    doc_contact=models.IntegerField()
    doc_password=models.CharField(max_length=50)
    doc_work=models.CharField(max_length=100)
    
# Create your models here.
