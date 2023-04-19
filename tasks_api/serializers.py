from rest_framework import serializers
from tasks_api import models


class TypeTaskSerializer(serializers.ModelSerializer):
    """Serializes Task Type Items"""

    class Meta:
        model = models.TypeTask
        fields = ('id', 'description')


class TaskSerializer(serializers.ModelSerializer):
    """Serializes Task Items"""

    class Meta:
        model = models.Task
        fields = (
            'id', 'user_profile', 'type_task', 'description', 'received_date', 'received_time', 'ticket', 'eta',
            'comments',
            'status')
        extra_kwargs = {
            'user_profile': {
                'read_only': True,
            }
        }
