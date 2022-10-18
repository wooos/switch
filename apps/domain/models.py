from email.policy import default
from enum import auto
from django.db import models


# Create your models here.
class Domain(models.Model):
    domain = models.CharField(max_length=128, null=False, unique=True)
    ipaddr = models.CharField(max_length=32, null=False)
    desc = models.CharField(max_length=128, default='')

    def __str__(self) -> str:
        return self.domain
