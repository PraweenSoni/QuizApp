from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    desc = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
