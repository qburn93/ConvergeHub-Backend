from django.urls import path
from posts import views
from posts.views import CategoryList

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
]