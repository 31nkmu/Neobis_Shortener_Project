from django.db import models


class Url(models.Model):
    url = models.URLField(unique=True)
    short_url = models.CharField(max_length=20, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

