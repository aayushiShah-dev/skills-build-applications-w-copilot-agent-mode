from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet, api_root
from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('', api_root, name='api-root'),  # Root endpoint
    path('admin/', admin.site.urls),  # Admin endpoint
    path('api/', include(router.urls)),  # API endpoint
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('teams/', views.TeamList.as_view(), name='team-list'),
    path('teams/<int:pk>/', views.TeamDetail.as_view(), name='team-detail'),
    path('activities/', views.ActivityList.as_view(), name='activity-list'),
    path('activities/<int:pk>/', views.ActivityDetail.as_view(), name='activity-detail'),
    path('leaderboard/', views.LeaderboardList.as_view(), name='leaderboard-list'),
    path('leaderboard/<int:pk>/', views.LeaderboardDetail.as_view(), name='leaderboard-detail'),
    path('workouts/', views.WorkoutList.as_view(), name='workout-list'),
    path('workouts/<int:pk>/', views.WorkoutDetail.as_view(), name='workout-detail'),
]
