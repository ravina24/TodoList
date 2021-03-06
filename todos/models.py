from django.db import models
from datetime import datetime

class Todo(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title # todolist object will now show as title instead of default name
