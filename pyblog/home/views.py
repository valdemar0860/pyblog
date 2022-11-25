from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home/index.html'

# def index(request):
#     # return HttpResponse("Hello World")
#     return render(request, 'templates/home/index.html')




