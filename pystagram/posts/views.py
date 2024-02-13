from django.shortcuts import render, redirect

# Create your views here.

def feeds(request):
    user = request.user
    is_authenticated = user.is_authenticated
    
    print("user: ", user)
    print("is_authenticated: ", is_authenticated)

    if not request.user.is_authenticated:
        print(user, "is_authenticated: ", is_authenticated)

        return redirect("/users/login/")

    return render(request, template_name="posts/feeds.html")
