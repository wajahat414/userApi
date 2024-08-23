from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} - {self.password}"
