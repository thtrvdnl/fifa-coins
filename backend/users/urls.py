from django.urls import path
from rest_framework.routers import DefaultRouter

from .api import views

app_name = 'users'

urlpatterns = [
    path('registration/', views.UserCreateAPIView.as_view()),
    path('', views.UserRetrieveUpdateDestroyAPIView.as_view())
]

