from django.db import models

class Application(models.Model):
    name     = models.CharField(max_length=50)
    target   = models.CharField(max_length=50, default='')
    place    = models.CharField(max_length=100, default='')
    time     = models.CharField(max_length=50, default='')
    contents = models.TextField()