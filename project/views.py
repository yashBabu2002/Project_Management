from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response    
from project.serializers import ProjectSerializer, TaskSerializer
from project.models import Project, Task
from authentication.permissions import IsAdminOrProjectManager



class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrProjectManager]
    

    def get_queryset(self):
        print(self.request.user)
        return Project.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        print(self.request.user)
        print(self.request.user.role)
        serializer.save(created_by=self.request.user)
        
        
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['project', 'status', 'priority', 'due_date']
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'priority', 'created_at']

    def get_queryset(self):
        user = self.request.user

        if user.role in ['admin', 'manager']:
            return Task.objects.filter(assigned_to__role='developer')
        else:
            return Task.objects.filter(assigned_to=user)
        
    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.role == 'developer' or request.user.role == 'manager':
            status_value = request.data.get('status')
            if not status_value:
                return Response({'error': 'Status is required.'}, status=status.HTTP_400_BAD_REQUEST)
            instance.status = status_value
            instance.save()
            return Response({'message': 'Status updated successfully.'})
        
        return super().update(request, *args, **kwargs)
    
        

    
    