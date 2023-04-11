from django.db import models
from django.utils import timezone


class Task(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_CHOICES = [
        (HIGH, 'Високий'),
        (MEDIUM, 'Середній'),
        (LOW, 'Низький'),
    ]

    title = models.CharField(max_length=255)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=LOW)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
