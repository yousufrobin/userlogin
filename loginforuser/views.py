from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request, "index.html")


def userlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, "login.html")

    return render(request, "login.html")


def userlogout(request):
    logout(request)
    return redirect("/login")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "This username already exists!")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email already exists!")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                messages.info(request, "You have successfully created a new user!")
                return redirect("/login")
        else:
            messages.info(request, "Passwords do not match")
            return redirect("register")

    else:
        return render(request, "register.html")


# def post and def dynamic is to understand dynamic url
def post(request, variable):
    return render(request, "post.html", {"context": variable})


def dynamic(request):
    variables = [1, 2, 3, "Yousuf", "Robin", "Robiul"]
    return render(request, "dynamic.html", {"context": variables})
