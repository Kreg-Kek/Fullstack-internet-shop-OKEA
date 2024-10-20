from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "OKEA - Главная"
        context["content"] = "Магазин мебели OKEA"
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "OKEA - О нас"
        context["content"] = "О нас"
        context["text_on_page"] = (
            "Здесь должно быть написанно о магазине, но я напишу о большой проделанной работе над сайтом. Фронтенд был написан на html и css, c использованием Bootstrap. В Бэкенде же было написанно 5 приложений: для главной страницы, для товаров и каталога, для корзин(с использованием джаваскрипта), для работы с пользователями и отдельно было вынесенно приложение для заказов. Реализована связь с базой данных Postgre SQL, в которой хранится информация о товарах и пользователях. Было реализовано кеширование для повышения оптимизации."
        )
        return context


# def index(request):

#     context = {
#         "title": "Home",
#         "content": "Магазин мебели OKEA",
#     }
#     return render(request, "main/index.html", context)


# def about(request):
#     context = {
#         "title": "О нас",
#         "content": "О нас",
#         "text_on_page": "Текст о том почему этот магазин крутой",
#     }
#     return render(request, "main/about.html", context)
