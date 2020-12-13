from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


# Create your models here.
class Car(models.Model):
    vin = models.CharField(verbose_name="vin", db_index=True, max_length=32)
    color = models.CharField(verbose_name="color", db_index=False, max_length=32)
    brand = models.CharField(verbose_name="brand", db_index=False, max_length=32)
    CAR_TYPES = ((1, "dj"), (2, "django"), (3, "rest"), (4, "framework"))
    Car_Type = models.IntegerField("Car_Type", choices=CAR_TYPES)
    Users = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE, )
