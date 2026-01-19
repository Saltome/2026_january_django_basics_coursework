from django.db import models

class Time(models.Model):
    value = models.FloatField(default=0)