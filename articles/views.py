from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Articles

# Create your views here.
class ArticleListView(LoginRequiredMixin, ListView):
    model = Articles
    template_name = 'article_list.html'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = 'article_detail.html'
    

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    # success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model= Articles
    template_name = 'new_article.html'
    fields = ('title', 'body',)
    
    def form_valid(self,form):
        form.instaance.author = form.request.user
        return super().form_valid(form)
