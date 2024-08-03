from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        # Get form values
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        # Check if passwords match
        if password != password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        # Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, "That username is taken")
            return redirect("register")

        # Check email
        if User.objects.filter(email=email).exists():
            messages.error(request, "That email is being used")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        # Login after register
        # auth.login(request, user)
        # messages.success(request, "You are now logged in")
        # return redirect("index")

        messages.success(request, "You are now registered and can log in")
        return redirect("login")

    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        print("SUBMITTED LOGIN")
        # Login User
        return
    else:
        return render(request, "accounts/login.html")


def logout(request):
    return redirect("index")


def dashboard(request):
    return render(request, "accounts/dashboard.html")
