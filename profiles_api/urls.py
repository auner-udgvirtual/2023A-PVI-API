from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views
from tasks_api import views as tasks_api_views

router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
router.register('task-type', tasks_api_views.TaskTypeViewSet)
router.register('tasks', tasks_api_views.TaskViewSet)

urlpatterns = [
    # path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
