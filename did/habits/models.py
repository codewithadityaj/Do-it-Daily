from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User
from django.db import models
from accounts.models import User

class Habit(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES)
    streak = models.IntegerField(default=0)
    last_completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name



