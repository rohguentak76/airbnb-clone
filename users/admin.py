# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    """ Custom User Admin """

    list_display = ("username", "gender", "language", "currency", "superhost")
    list_filter = (
        "language",
        "currency",
        "superhost",
    )


# admin.site.register(models.User, CustomUserAdmin)
