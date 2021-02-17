from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):  ## inherit AbstractUser class
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

    avatar = models.ImageField(blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
    )  ## one line width maximum
    bio = models.TextField(default="", blank=True)  ##multiple line is available
    # bio = models.TextField( // null value is posible in db

    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, blank=True, max_length=10)

    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=10, blank=True)

    superhost = models.BooleanField(default=False)

    # def __str__(self):
    #    return self.username
