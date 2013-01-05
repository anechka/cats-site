# coding: utf-8
from django.shortcuts import render_to_response

dataTable = ({'name': 'Mosha', 'age': 24, 'billingOut': 350}, {'name': 'Вася', 'age': 12, 'billingOut': 300})

def index(request):
    return render_to_response("index.html", {'cats_data':dataTable})