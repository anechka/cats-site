# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext

from cats.models import Cat

#dataTable = ({'name': 'Mosha', 'age': 24, 'billingOut': 350}, {'name': 'Вася', 'age': 12, 'billingOut': 300})

def index(request):
    # Создаём котов, итерируемый объект, получаемый собиранием данных из БД sqlite
    cats = Cat.objects.all()

    return render_to_response("index.html", {'cats_data':cats}, context_instance=RequestContext(request))
    # Передаём 3-им параметром инстанс класса RequestContext. В то время, как в обычной ситуации передаётся django.template.Context, мы же передадим другой аналогичный класс RequestContext
    # В котором хранится набор переменных, получаемых из настроек Django для рендеринга шаблонов
    # Одной из таких переменных-настроек является "django.core.context_processors.static"
    # Другими словами, в шаблоны HTML передаётся возможность вставлять ссылки на статичные файлы,
    # настройки которых прописаны в cats.settings главном модуле настроек.

    # -> RequestContext: The second difference is that it automatically populates the context with a few variables, according to your TEMPLATE_CONTEXT_PROCESSORS setting.
    #    By default, TEMPLATE_CONTEXT_PROCESSORS is set to:
    #    ("django.contrib.auth.context_processors.auth",
    #     "django.core.context_processors.debug",
    #     "django.core.context_processors.i18n",
    #     "django.core.context_processors.media",
    #     "django.core.context_processors.static",
    #     "django.contrib.messages.context_processors.messages")
