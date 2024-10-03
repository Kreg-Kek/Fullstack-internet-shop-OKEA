from django.shortcuts import render


def login(request):
    context = {"title": "OKEA - Авторизация"}
    return render(request, "users/login.html", context)


def registration(request):
    context = {"title": "OKEA - Регистрация"}
    return render(request, "users/registration.html", context)


def profile(request):
    context = {"title": "OKEA - Кабинет"}
    return render(request, "users/profile.html", context)


def logout(request):
    pass
