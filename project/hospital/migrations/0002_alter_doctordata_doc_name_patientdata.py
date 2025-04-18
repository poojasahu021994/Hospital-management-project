# Generated by Django 5.1.7 on 2025-04-12 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordata',
            name='doc_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('patient_email', models.EmailField(max_length=254)),
                ('patient_add', models.CharField(max_length=50)),
                ('patient_DOB', models.DateField()),
                ('patient_contact', models.IntegerField()),
                ('patient_password', models.CharField(max_length=50)),
                ('patient_cpassword', models.CharField(max_length=50)),
                ('patient_details', models.CharField(max_length=100)),
                ('add_dep', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.department', to_field='dep_name')),
                ('select_doc', models.ManyToManyField(to='hospital.doctordata')),
            ],
        ),
    ]
