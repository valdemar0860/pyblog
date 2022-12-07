from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponse

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home/index.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'home/post_detail.html'
    context_object_name = 'view_blog_detail'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'home/post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'home/post_edit.html'


# def index(request):
#     # return HttpResponse("Hello World")
#     return render(request, 'templates/home/index.html')




