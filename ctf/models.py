from django.db import models


class DoneIt(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
