from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_blog(request):
    return HttpResponse("testing")