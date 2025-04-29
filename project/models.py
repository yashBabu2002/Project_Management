from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_projects')
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('To-Do', 'To-Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To-Do')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Low')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title