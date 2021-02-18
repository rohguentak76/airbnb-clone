from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """message admin definition """

    pass


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """conversation admin definition """

    pass