from django.urls import path
from . import views

app_name='discussion_app'

urlpatterns = [
    path('<int:id>/', views.category_detail, name='category_detail'),
]
