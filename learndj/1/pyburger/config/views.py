from django.http import HttpResponse
from django.shortcuts import render

from burgers.models import Burger

def main(request):
    # return HttpResponse("안녕하세요,  파이버거입니다.")
    return render(request, "main.html")


def burger_list(request):
    # return HttpResponse("파이버거의 햄버거 목록입니다.")
    blist = Burger.objects.all()
    print(blist)

    context = {
        "burger_list" : blist
    }
    return render(request, "burger_list.html", context=context)

def burger_search(request):
    key = request.GET.get('key')
    if key is None or len(key) == 0:
        blist = Burger.objects.none()
        print('key is None', blist)
    else:
        blist = Burger.objects.filter(name__contains=key)

    context = { "burger_list": blist }
    print("key:", key, context)
    return render(request=request, template_name="burger_search.html", context=context)
#