"""baike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from api import views
from django.contrib import admin
from django.urls import path, re_path, include
from django.views import static
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


urlpatterns = [
    path('',views.index),
    path('admin/', admin.site.urls),
    path('articles/', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article-search/', views.ArticleSearchView.as_view(), name='article-search'),
    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': os.path.join(BASE_DIR, 'static')}),
    path('index/',views.index),
    path('detail/', views.detail),
    path('search/', views.search),
    path('about/', views.about),
    path('contact/', views.contact),
]
