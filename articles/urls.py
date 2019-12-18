from django.urls import path
from .views import ArticleListView, CommentCreateView, ArticleUpdateView, ArticleDetailView,  ArticleDeleteView, ArticleCreateView, fbv_article_detail

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('<int:pk>/comment/new/', CommentCreateView.as_view(), name='add-comment'),

    path('new/', ArticleCreateView.as_view(), name='article-new'),
    path('', ArticleListView.as_view(), name='article-list'),

    path('fbv/', fbv_article_detail, name='fbv_article_detail')


]
