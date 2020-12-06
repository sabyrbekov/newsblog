from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'articles_app'


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('kyrgyzstan/', views.KyrgyzstanArticleListView.as_view(), name='kg_article_list'),
    path('world/', views.WorldArticleListView.as_view(), name='world_article_list'),
    path('sport/', views.SportArticleListView.as_view(), name='sport_article_list'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
