from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    
    # FIX (3) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.text
