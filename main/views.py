from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"title": "Home", "content": "Магазин мебели OKEA"}
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "О нас",
        "content": "О нас",
        "text_on_page": "Текст о том почему этот магазин крутой",
    }
    return render(request, "main/about.html", context)
