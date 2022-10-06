# hello_django/calc/views.py
from django.http import HttpResponse
def index(request):
    return HttpResponse('Yes')