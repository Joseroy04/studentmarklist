from django.contrib import admin

# Register your models here.
from  .models import studentData,Pedagogy

admin.site.register(studentData)
admin.site.register(Pedagogy)