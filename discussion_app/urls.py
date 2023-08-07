from django.urls import path
from . import views

app_name='discussion_app'

urlpatterns = [
    path('<int:id>/', views.category_detail, name='category_detail'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/like/<int:id>/', views.post_like, name='post_like'),
    path('post/comment-like/<int:id>/', views.comment_like, name='comment_like'),
    path('post/post-save/<int:id>/', views.post_save, name='post_save'),
    path('post/create-post/', views.create_post, name='create_post'),
    path('post/delete-post/<int:id>', views.delete_post, name='post_delete'),
    path('post/edit-post/<int:id>', views.edit_post, name='post_edit'),
    path('posts/search/', views.search_posts, name='search_posts'),
    
]
