from urllib.parse import urlparse
from django.urls import path
from .views import HomeView, ArticalDetailView, AddPostView, UpdatePostViews,DeletePostView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticalDetailView.as_view(), name="article-details"),
    path('add_post/', AddPostView.as_view(), name= 'add_post' ),
    path('article/edit/<int:pk>', UpdatePostViews.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]
