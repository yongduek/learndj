from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        redirect("/posts/feeds/")

    return render(request, "users/login.html")
