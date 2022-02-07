from django.db import models
#from django.contrib.auth.models import User
from django.db.models.base import Model
from django.contrib.auth import get_user_model

import uuid

User = get_user_model()
from config.utils.models import Entity




class Profile(Entity):
    name = models.CharField("Name",max_length=255,null=True)
    age = models.CharField("age",max_length=100)
    weight = models.CharField("Weight",max_length=100)
    gender = models.CharField("Gender",max_length=100,choices=[("male","male"),("fmale","fmale")])
    number = models.CharField(verbose_name="Number",max_length=100)
    Ward = models.CharField("Ward",max_length=100)
    Bed = models.CharField("Bed",max_length=100)
    diagnoses = models.CharField("Diagnoses",max_length=255)
    operation_type = models.CharField("Operation Type",max_length=255)
    entry_date_time = models.DateTimeField("entry date time",auto_now_add=True)
    operation_date_time = models.DateTimeField("operation date time",auto_now_add=False)
    leaving_date_time = models.DateTimeField("leaving date time",auto_now_add=False)
    medications = models.TextField("Medications")
    operative_finding = models.TextField("operative finding",max_length=255)
    operative_procedure = models.TextField("operative procedure",max_length=255)
    operative_note = models.TextField("operative note",max_length=255)
    specimen_to_laboratory = models.BooleanField("specimen to laboratory")
    consultant_surgeon = models.CharField("consultant surgeon",max_length=255)
    co_surgeon = models.CharField("co_surgeon",max_length=255)
    surgeon = models.CharField("surgeon",max_length=255)
    anesthetist =models.CharField("anesthetist",max_length=255)
    nurse = models.CharField("nurse",max_length=255)
    sponge_nurse = models.CharField("sponge_nurse",max_length=255)
    doctor_name = models.CharField("doctor_name",max_length=255)
    added_by = models.ForeignKey(User,verbose_name="Added By",on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return self.name



