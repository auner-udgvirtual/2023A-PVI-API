from django.db import models
from django.conf import settings


class TypeTask(models.Model):
    """Type of tasks being used"""
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        """Return the model as string"""
        return self.description


class Task(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type_task = models.ForeignKey(TypeTask, on_delete=models.CASCADE)
    description = models.CharField(max_length=150, blank=False)
    received_date = models.DateField()
    received_time = models.TimeField(blank=True, null=True)
    ticket = models.CharField(max_length=50, blank=True, null=True)
    eta = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, default="active")

