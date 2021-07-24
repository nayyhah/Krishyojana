from django.urls import path, include
from .views import (
	PostListView,
    UserPostListView,
	ProfileDetailView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='krish-home'),
    path('schemes/', include('schemes.urls')),
    path('emarket/', PostListView.as_view(), name='krish-emarket'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('msp/', views.msp, name='krish-msp')
]