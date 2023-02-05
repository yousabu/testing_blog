from django.urls import path
from urllib.parse import urlparse
from .views import UserRegisterView
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserRegisterView.as_view(), name='login'),
]
