from django.urls import path
from . import views

app_name='discussion_app'

urlpatterns = [
    path('<int:id>/', views.category_detail, name='category_detail'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/like/<int:id>/', views.post_like, name='post_like'),
    
]
