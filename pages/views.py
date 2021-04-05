from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    """ """
    return render(request, 'pages/index1.htm')
    # return HttpResponse('<h1>Hello world</h1>')
    

def about(request):
    return render(request, 'pages/about.htm')