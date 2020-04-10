from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from django.utils import timezone
from django.contrib import messages

# Create your views here.
def home(request):
    allPost = Post.objects.all()
    context = {'allPost': allPost}
    return render(request, 'home/home.html', context)


def dashboard(request):
    return HttpResponse('You are visiting the dashboard')


def post(request):
    if request.method == 'POST':

        topic = request.POST['topic']
        description = request.POST['description']
        author = request.POST['author']

        if topic == '' or description == '' or author == '':
            messages.warning(request, "Please enter valid information")
        else:
            newPost = Post(topic=topic, description=description, author=author, date_created=timezone.now())
            newPost.save()
            messages.success(request, "Your Post has been created successfully")

    else:
        messages.error(request, "Error while submitting!!!")

    return render(request, 'home/post.html')