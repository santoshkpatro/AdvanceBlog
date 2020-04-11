from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pwd1 = request.POST['Password1']
        pwd2 = request.POST['Password2']
        if firstname == '' or lastname == '' or email == '' or pwd1 == '' or pwd2 == '':
            messages.warning(request, "Please enter valid informantion")
        else:
            if pwd1 == pwd2:
                newUser = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=pwd1)
                newUser.save()
                messages.success(request, "Account created successfully!!!")

    return render(request, 'accounts/signup.html')