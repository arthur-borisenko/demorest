from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Click(models.Model):
    button = models.CharField(verbose_name="button", db_index=False, max_length=32)
    BTH_TYPES=((1,'LEFT'),(2,"WHEEL"),(3,'RIGHT'))
    which = models.IntegerField(verbose_name="which", db_index=False,choices=BTH_TYPES)
    Users = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE, )