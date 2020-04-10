from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def home(request):
    allPost = Post.objects.all()
    context = {'allPost': allPost}
    return render(request, 'home/home.html', context)