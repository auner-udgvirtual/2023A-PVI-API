from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from tasks_api import serializers
from tasks_api import models
from profiles_api import permissions


class TaskTypeViewSet(viewsets.ModelViewSet):
    """Handles CRUD Task Type items"""

    serializer_class = serializers.TypeTaskSerializer
    queryset = models.TypeTask.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    """Handles CRUD Task items"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.filter(status='active')

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)