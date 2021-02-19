from django.db import models
from core import models as core_models

# Create your models here.
class Review(core_models.TimeStampedModel):
    """review model definitions """

    review = models.TextField()
    Accuracy = models.IntegerField()
    Communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="review", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="review", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"
