from django.db import models

class Department(models.Model):
    dep_name=models.CharField(max_length=50, unique=True)
    dep_description=models.CharField(max_length=50)
    dep_Hod=models.CharField(max_length=50)
    def __str__(self):
        return self.dep_description

class DoctorData(models.Model):
    doc_name=models.CharField(max_length=50)
    doc_email=models.EmailField()
    doc_DOJ=models.DateField()
    doc_dep=models.ForeignKey(Department,on_delete=models.PROTECT, to_field='dep_name')
    doc_Que=models.CharField(max_length=50)
    doc_contact=models.IntegerField()
    doc_password=models.CharField(max_length=50)
    doc_work=models.CharField(max_length=100)
    
# Create your models here.
