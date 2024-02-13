from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        redirect("/posts/feeds/")
    else:
        redirect("/users/login/")

#    return render(request, "index.html")
