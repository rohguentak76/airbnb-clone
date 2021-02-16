# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    # list_display = ("username", "gender", "language", "currency", "superhost", "email")
    # list_filter = (
    #    "language",
    #    "currency",
    #    "superhost",
    # )


# admin.site.register(models.User, CustomUserAdmin)
