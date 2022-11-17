from django.db import models


class Webhook(models.Model):
    event = models.CharField(max_length=254, blank=True)
    timestamp = models.PositiveIntegerField(null=True)
    payload = models.TextField()
