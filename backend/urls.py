from backend.views.post_view import PostView
from django.urls import path

from backend.views.user_view import UserView

urlpatterns = [
    path('posts/', PostView.as_view({'get': 'list', 'post': 'create'}), name='api-post-create-list'),
    path('posts/<str:pk>/', PostView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'}),
         name='api-post-update-get-delete'),
    path('user/', UserView.as_view({'get': 'get_user'}), name="api-user-update-get")
]
