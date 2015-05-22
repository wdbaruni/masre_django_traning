from django.contrib import admin
from CWE.models import *
# Register your models here.


class CWEAdmin(admin.ModelAdmin):
    fields = ['code', 'name']

admin.site.register(CWE, CWEAdmin)
