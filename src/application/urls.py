from django.urls import path
from . import views


app_name = 'application'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='all-posts'),
    path('posts/<int:pk>', views.post_detail, name='post-detail'),
    path('posts/create/', views.create_post, name='post-create'),
    path('<int:year>/<str:month>/', views.home, name='calendar-page'),
]
