# accounts/urls.py
from django.urls import path

from .views import SignUpView
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', views.update_profile, name='update_profile'),
]