from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=150, default='Project')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    done_per_cent = models.PositiveIntegerField(default=0)
    date_create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class TODO(models.Model):
    name = models.CharField(max_length=150)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    is_done = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name