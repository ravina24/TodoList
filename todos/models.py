from django.db import models
from datetime import datetime

class Todo(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #!!!created_at = models.DateTimeField(default=datetime.now, blank=True)
