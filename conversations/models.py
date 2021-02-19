from django.db import models
from core import models as core_models

# Create your models here.


class Conversation(core_models.TimeStampedModel):
    """conversation model definition"""

    participants = models.ManyToManyField(
        "users.User", related_name="conversation", blank=True
    )

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="message", on_delete=models.CASCADE
    )
    Conversation = models.ForeignKey(
        "Conversation", related_name="message", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} - {self.text}"
