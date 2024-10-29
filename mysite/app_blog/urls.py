# app_blog/urls.py
from django.urls import path
from .views import (HomePageView, ArticleDetail, 
                    ArticleList, ArticleCategoryList)
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('articles/', ArticleList.as_view(), name='articleslist'),
    path('articles/category/<slug:category_slug>/', 
         ArticleCategoryList.as_view(), 
         name='articles-category-list'),
    path('articles/<int:year>/<int:month>/<int:day>/<slug:slug>/', 
         ArticleDetail.as_view(), 
         name='news-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
