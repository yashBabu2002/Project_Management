from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers
from project.models import Project, Task


User = get_user_model()


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['id', 'created_by']
        
class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'project', 'assigned_to',
            'due_date', 'status', 'priority', 'created_at', 'updated_at'
        ]

    def validate(self, data):
        if data['due_date'] < timezone.now():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return data

    