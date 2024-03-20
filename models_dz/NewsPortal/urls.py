from django.urls import path

from django.contrib import admin
from django.urls import path, include
from .views import NewsList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, subscriptions

urlpatterns = [

    path('post/', NewsList.as_view(), name='news_list'),
    path('post/search/', PostSearch.as_view(), name='post_search'),
    path('post/<int:pk>/', PostDetail.as_view()),
    path('news/create', PostCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/delete/', PostDelete.as_view(), name='articles_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),

]
