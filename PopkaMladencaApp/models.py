from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class CustomUser(User):
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=12)

    def __str__(self):
        return self.phone_number
