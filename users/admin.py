# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
