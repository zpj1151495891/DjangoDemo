from django.contrib import admin
from . import models


# Register your models here.


class student_admin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'born', 'like']


admin.site.register(models.student, student_admin)
