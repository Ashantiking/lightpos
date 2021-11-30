from django.contrib import admin
from .models import Company, Developer, Staff

# Register your models here.

admin.site.register(Company)
admin.site.register(Developer)
admin.site.register(Staff)
