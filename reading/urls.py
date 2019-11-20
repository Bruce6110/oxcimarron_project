from django.urls import path
from .views import AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView, BookCreateView, BookUpdateView, BookDeleteView
from . import views

# note, the include() function in the project urls file prepends "reading" to these patterns

# for class-based views, the as_view method converts the class to a view
urlpatterns = [
    path('books-by-year', views.books_by_year, name='books-by-year'),
    path('pages-by-year', views.pages_by_year, name='pages-by-year'),
    path('book/<int:pk>/update', BookUpdateView.as_view(),  name='book-update'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(),  name='book-delete'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('', views.home, name='book-list'),
    path('author/<int:pk>/update',
         AuthorUpdateView.as_view(),  name='author-update'),
    path('author/<int:pk>/delete',
         AuthorDeleteView.as_view(),  name='author-delete'),
    path('author/new/', AuthorCreateView.as_view(), name='author-create'),
    path('authors', AuthorListView.as_view(),  name='author-list'),



    # <app>/<model>_<viewtype>.html
]
