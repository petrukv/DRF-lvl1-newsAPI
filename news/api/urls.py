from django.urls import path

from news.api.views import *

urlpatterns = [
    path('articles/', article_list_create_api_view, name='article-list'),
    path('articles/<int:pk>/', article_detail_api_view, name='article-detail'),
]
