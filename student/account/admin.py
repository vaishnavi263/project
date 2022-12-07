from django.contrib import admin
from .models import Course,Contact,Staff

# Register your models here.
admin.site.register(Course)
admin.site.register(Staff)   
class Customerdetails(admin.ModelAdmin):
    list_display=('name','phno','email')
admin.site.register(Contact,Customerdetails) 
