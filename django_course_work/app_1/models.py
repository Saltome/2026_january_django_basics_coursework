from django.db import models

class Time(models.Model):
    value = models.IntegerField(default=0)
