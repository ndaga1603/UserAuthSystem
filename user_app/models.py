from django.db import models
from django.contrib.auth.models import AbstractUser
import random


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True)


class Code(models.Model):
    code = models.CharField(max_length=5)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        random_integers = [random.randint(1, 10) for _ in range(5)]
        code_string = "".join([str(integer) for integer in random_integers])

        self.code = code_string

        return super().save(*args, **kwargs)
