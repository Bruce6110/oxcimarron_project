from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    # we exclude 'author' because it should be auto-entered as username)
    form_class = ArticleForm
    #fields = ('title', 'body', 'image')
    template_name = 'articles/article_new.html'
    login_url = '/users/login'

    def form_valid(self, form):
        print("ACV form_val")
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class=CommentForm
    template_name = 'articles/article_detail.html'
    #fields = ['comment','uthor']
    login_url = '/users/login'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'articles/article_edit.html'
    form = ArticleForm
    fields = ('title', 'body', 'image')
    login_url = '/users/login'

    def test_func(self):
        obj = self.get_object()
        print("AUV test_func")
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    # 'success_url' is for when you want to redirect upon success
    success_url = reverse_lazy('article-list')
    login_url = '/users/login'
