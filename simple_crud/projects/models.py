from django.db import models

class Project(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField(blank=True)
    technology=models.CharField(max_length=200)
    created_at= models.DateTimeField(auto_now_add=True)