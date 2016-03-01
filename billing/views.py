# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Cat


def index(request):
    cats = Cat.objects.all()

    return render_to_response("index.html", {'cats_data': cats}, context_instance=RequestContext(request))
    # Передаём 3-им параметром инстанс класса RequestContext.
    # В то время, как в обычной ситуации передаётся django.template.Context,
    # мы же передадим другой аналогичный класс RequestContext
    # В котором хранится набор переменных, получаемых из настроек Django для рендеринга шаблонов
    # Одной из таких переменных-настроек является "django.core.context_processors.static"
    # Другими словами, в шаблоны HTML передаётся возможность вставлять ссылки на статичные файлы,
    # настройки которых прописаны в cats.settings главном модуле настроек.