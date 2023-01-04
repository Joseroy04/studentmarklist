from django.contrib import admin

# Register your models here.
from  .models import studentData,Pedagogy,Deportment

admin.site.register(studentData)
admin.site.register(Deportment)
admin.site.register(Pedagogy)