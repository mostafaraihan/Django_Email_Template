from django.urls import path
from .views import signup_view,mass

urlpatterns = [
    path("", signup_view, name="signup"),
]
