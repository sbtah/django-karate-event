from django.urls import path
from . import views


app_name = 'application'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='all-posts'),
    path('posts/<int:pk>', views.post_detail, name='post-detail'),
    path('posts/create/', views.create_post, name='post-create'),
    path('posts/update/<int:pk>/',
         views.update_post, name='update-post'),
    path('posts/delete-location/<int:pk>/',
         views.delete_post, name='delete-post'),
]
