from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks_api import views

router = DefaultRouter()
router.register('task-type', views.TaskTypeViewSet)
router.register('tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
