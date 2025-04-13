from django.db import models

# class Department(models.Model):
#     dep_name=models.CharField(max_length=50, unique=True)
#     dep_description=models.CharField(max_length=50)
#     dep_Hod=models.CharField(max_length=50)
#     def __str__(self):
#         return self.dep_description

# class DoctorData(models.Model):
#     doc_name=models.CharField(max_length=50,unique=True)
#     doc_email=models.EmailField()
#     doc_DOJ=models.DateField()
#     doc_dep=models.ForeignKey(Department,on_delete=models.PROTECT, to_field='dep_name')
#     doc_Que=models.CharField(max_length=50)
#     doc_contact=models.IntegerField()
#     doc_password=models.CharField(max_length=50)
#     doc_work=models.CharField(max_length=100)

# class PatientData(models.Model):
#     patient_name=models.CharField(max_length=50)
#     patient_email=models.EmailField()
#     patient_add=models.CharField(max_length=50)
#     patient_DOB=models.DateField()
#     add_dep=models.ForeignKey(Department,on_delete=models.PROTECT, to_field='dep_name')
#     patient_contact=models.IntegerField()
#     select_doc=models.ManyToManyField(DoctorData)
#     patient_password=models.CharField(max_length=50)
#     patient_cpassword=models.CharField(max_length=50)
#     patient_details=models.CharField(max_length=100)    
    
# Create your models here.

from django.db import models

class Department(models.Model):
    dep_name = models.CharField(max_length=50, unique=True)
    dep_description = models.CharField(max_length=50)
    dep_Hod = models.CharField(max_length=50)

    def __str__(self):
        return self.dep_description


class DoctorData(models.Model):
    doc_name = models.CharField(max_length=50, unique=True)
    doc_email = models.EmailField()
    doc_DOJ = models.DateField()
    doc_dep = models.ForeignKey(Department, on_delete=models.PROTECT, to_field='dep_name')
    doc_Que = models.CharField(max_length=50)
    doc_contact = models.BigIntegerField()  # Changed to BigInteger for phone numbers
    doc_password = models.CharField(max_length=50)
    doc_work = models.CharField(max_length=100)

    def __str__(self):
        return self.doc_name


class PatientData(models.Model):
    patient_name = models.CharField(max_length=50)
    patient_email = models.EmailField(unique=True)  # Recommended to prevent duplicate users
    patient_add = models.CharField(max_length=50)
    patient_DOB = models.DateField() 
    patient_contact = models.BigIntegerField()  # Changed to BigInteger
    patient_password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.patient_name
    
class BookingData(models.Model):
    P_name=models.CharField(max_length=50)
    P_email=models.EmailField()
    P_address=models.CharField(max_length=50)
    P_DOB=models.CharField(max_length=50)
    P_contact=models.BigIntegerField()
    P_details = models.CharField(max_length=100)
    add_dep = models.ForeignKey(Department, on_delete=models.PROTECT, to_field='dep_name')
    select_doc = models.ManyToManyField(DoctorData)
