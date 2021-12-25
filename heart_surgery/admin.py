from django.contrib import admin

from heart_surgery.models import Profile,Diagnoses_Date_Medications,Operation_Info,Doctors_and_Staff

admin.site.register(Profile)
admin.site.register(Diagnoses_Date_Medications)
admin.site.register(Operation_Info)
admin.site.register(Doctors_and_Staff)


