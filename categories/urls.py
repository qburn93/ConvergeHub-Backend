from django.urls import path
from posts import views
from posts.views import CategoryList


urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category-list'),
]