from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length = 50)
    user_id = models.CharField(max_length = 50, default='')
    password = models.CharField(max_length = 200)
    group = models.CharField(max_length = 50, default='')
    admin = models.BooleanField(default=False)
    token = models.CharField(max_length = 200, default='')
    work_status = models.CharField(max_length = 50, default='')
    created_at = models.DateTimeField(auto_now_add=True)