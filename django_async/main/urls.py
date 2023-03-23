from django.urls import path
from main import views

urlpatterns = [
    path('check-health/', views.CheckHealth.as_view(), name="check_health"),
    path('user/', views.UserApiView.as_view(), name="user"),
]