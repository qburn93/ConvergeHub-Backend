from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileViewSet.as_view())
]