from django.urls import path
from .views import ArticleListView, CommentCreateView, ArticleUpdateView, ArticleDetailView,  ArticleDeleteView, ArticleCreateView

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('comment/new/', CommentCreateView.as_view(), name='add-comment'),

    path('new/', ArticleCreateView.as_view(), name='article-new'),
    path('', ArticleListView.as_view(), name='article-list'),


]
