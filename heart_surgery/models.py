from django.db import models


class Profile(models.Model):
    name = models.CharField("Name",max_length=255)
    age = models.CharField("age",max_length=100)
    weight = models.IntegerField("Weight",)
    gender = models.CharField("Gender",max_length=100,choices=[("male","male"),("fmale","fmale")])
    number = models.AutoField(primary_key=True,verbose_name="Number",unique=True,auto_created=True)
    Ward = models.CharField("Ward",max_length=100)
    Bed = models.CharField("Bed",max_length=100)

    def __str__(self) -> str:
        return self.name

class Diagnoses_Date_Medications(models.Model):
    diagnoses = models.CharField("Diagnoses",max_length=255)
    operation_type = models.CharField("Operation Type",max_length=255)
    entry_date_time = models.DateTimeField("entry date time",auto_now_add=True)
    operation_date_time = models.DateTimeField("operation date time",auto_now_add=False)
    leaving_date_time = models.DateTimeField("leaving date time",auto_now_add=False)
    medications = models.TextField("Medications")
    patient = models.ForeignKey(Profile,related_name="Diagnoses_Date_Medications",on_delete=models.CASCADE,verbose_name="patient")
    def __str__(self) -> str:
        return self.diagnoses

class Operation_Info(models.Model):
    operative_finding = models.CharField("operative finding",max_length=255)
    operative_procedure = models.CharField("operative procedure",max_length=255)
    operative_note = models.CharField("operative note",max_length=255)
    specimen_to_laboratory = models.BooleanField("specimen to laboratory")
    patient = models.ForeignKey(Profile,related_name="Operation_Info",on_delete=models.CASCADE,verbose_name="patient")

    def __str__(self) -> str:
        return self.operative_finding




class Doctors_and_Staff(models.Model):
    consultant_surgeon = models.CharField("consultant surgeon",max_length=255)
    co_surgeon = models.CharField("co_surgeon",max_length=255)
    surgeon = models.CharField("surgeon",max_length=255)
    anesthetist =models.CharField("anesthetist",max_length=255)
    nurse = models.CharField("nurse",max_length=255)
    sponge_nurse = models.CharField("sponge_nurse",max_length=255)
    doctor_name = models.CharField("doctor_name",max_length=255)
    patient = models.ForeignKey(Profile,related_name="Doctors_and_Staff",on_delete=models.CASCADE,verbose_name="patient")

    def __str__(self) -> str:
        return self.consultant_surgeon