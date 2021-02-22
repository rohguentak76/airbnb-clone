from django.contrib import admin
from . import models

# Register your models here.


@admin.register(
    models.RoomType,
    models.Facility,
    models.Amenity,
    models.HouseRule,
)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        (
            "Times",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                )
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "guests",
                    "beds",
                    "bedrooms",
                    "baths",
                )
            },
        ),
        (
            "More About the space",
            {
                "classes": ("collapse",),
                "fields": (
                    "Amenities",
                    "facilities",
                    "house_rule",
                ),
            },
        ),
        (
            "Host",
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photoes",
        "total_rating",
    )
    ordering = ("name", "price", "bedrooms")
    list_filter = (
        "instant_book",
        "host__gender",  # get foreignkey
        "city",
        "room_type",
        "Amenities",
        "facilities",
        "house_rule",
        "country",
    )

    search_fields = ["city", "^host__username", "host__gender"]
    filter_horizontal = (  # for manytomany
        "Amenities",
        "facilities",
        "house_rule",
    )

    def count_amenities(self, object):  # self = RoomAdmin object = current row
        return object.Amenities.count()

    count_amenities.short_description = "amenities number"

    def count_photoes(self, obj):
        return obj.photo.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """photo admin definition """

    pass
