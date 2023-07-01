from django.urls import  path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from . import forms

app_name = 'core_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='core_app/login.html', 
                                     authentication_form=forms.LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]