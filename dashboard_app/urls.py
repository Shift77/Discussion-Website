from django.urls import path
from . import views

app_name = 'dashboard_app'

urlpatterns = [
    path('<int:id>', views.dashboard_detail, name='dashboard')
]