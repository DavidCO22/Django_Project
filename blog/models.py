from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class project_model(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_model = models.ForeignKey(project_model, on_delete=models.CASCADE)

class tareas(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    available = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title



