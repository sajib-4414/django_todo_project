from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def get_index_page(request):
    return HttpResponse('hello world')
