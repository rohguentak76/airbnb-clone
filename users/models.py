from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = {
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    }

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"
    LANGUAGE_CHOICES = {(LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean")}

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = {(CURRENCY_KRW, "KRW"), (CURRENCY_USD, "USD")}

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True
    )  ## one line width maximum
    bio = models.TextField(default="", blank=True)  ##multiple line is available
    # bio = models.TextField(null=TRUE) // null value is posible in db

    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, null=True, blank=True, max_length=10
    )

    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=10, null=True, blank=True
    )

    superhost = models.BooleanField(default=False)
