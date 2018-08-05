from django.db import models
from datetime import datetime
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):#this creates a representation of Todoclass object, suppose we have a row in django, then row will be represented by what this method returns
        return self.title
