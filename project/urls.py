from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]
