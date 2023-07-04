from django.db import models

# Create your models here.


class Subscribe(models.Model):
    email = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f"{self.email}"
