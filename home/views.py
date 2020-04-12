from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    allPost = Post.objects.all()
    context = {'allPost': allPost}
    return render(request, 'home/home.html', context)


@login_required(login_url='userlogin')
def dashboard(request, user_id):
    user = User.objects.get(id=user_id)
    allpost = user.post_set.all()
    context = {'allpost': allpost}
    return render(request, 'home/dashboard.html', context)


@login_required(login_url='userlogin')
def post(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        topic = request.POST['topic']
        description = request.POST['description']

        if topic == '' or description == '':
            messages.warning(request, "Please enter valid information")
        else:
            newPost = Post(user=user, topic=topic, description=description, date_created=timezone.now())
            newPost.save()
            messages.success(request, "Your Post has been created successfully")

    return render(request, 'home/post.html')