from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from oxcimarron.utils import Utils
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.shortcuts import render, get_object_or_404
import sys, traceback

def fbv_article_detail(request, slug):
    print("VIEW INITIATED: fbv detail")
    template_name = 'fbv_article_detail.html'
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            print("Comment form is valid.")

            # Create comment object but don't save to db
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
        else:
            comment_form = CommentForm()

        return render(request, template_name, {'article': article, 'comments': comments,
                                               'new_comment': new_comment,
                                               'comment_form': comment_form})


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
    form_class = CommentForm
    template_name = 'articles/add_comment.html'
    #template_name = 'articles/test.html'
    #fields = ['comment','author']
    login_url = '/users/login'

    def form_valid(self, form):
        print("PRINTING CCV props")
        print(":::", Utils.getAttributeReport(self))
        return super(CommentCreateView, self).form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'articles/article_edit.html'
    form = ArticleForm
    fields = ('title', 'body', 'image')
    login_url = '/users/login'

    def test_func(self):
        obj = self.get_object()
        print("AUV test_func: ", str(obj.author) +
              " vs. "+str(self.request.user))
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    # 'success_url' is for when you want to redirect upon success
    success_url = reverse_lazy('article-list')
    login_url = '/users/login'
