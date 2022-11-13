from django.shortcuts import render
from article.models import Post, Topic
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from article.forms import PostForm


def index(request):
    ads = Post.objects.order_by('-published')
    return render(request, 'index.html', {'ads': ads})


class PostCreateView(CreateView):
    template_name = 'create.html'
    form_class = PostForm
    success_url = reverse_lazy('article:list')


class PostUpdateView(UpdateView):
    template_name = 'create.html'
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('article:list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('article:list')
