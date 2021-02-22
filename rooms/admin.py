from django.contrib import admin
from django.utils.html import mark_safe
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


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin definition """

    inlines = (PhotoInline,)
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
    raw_id_fields = ("host",)
    search_fields = ["city", "^host__username", "host__gender"]
    filter_horizontal = (  # for manytomany
        "Amenities",
        "facilities",
        "house_rule",
    )

    def save_model(self, request, obj, form, change):
        print(obj, change, form)
        super().save_model(request, obj, form, change)

    def count_amenities(self, object):  # self = RoomAdmin object = current row
        return object.Amenities.count()

    count_amenities.short_description = "amenities number"

    def count_photoes(self, obj):
        return obj.photo.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """photo admin definition """

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        print(obj.file)
        return mark_safe(f'<img  width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"