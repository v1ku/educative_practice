from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):

    my_dict = {'insert_me': "Hello I am from views.py!"}
    return render(request, 'first_app/index.html', context=my_dict)

def home(request):
    return HttpResponse("Welcome to home page!")

def educative(request):
    return HttpResponse("Welcome to Educative page!")


def show_age(request, age):
    return HttpResponse("I am %s years old." % age)

def even_or_odd(request, num):
    if(num%2==0):
        output="%s is an even number." % num
    else:
        output="%s is an odd number." % num
    return HttpResponse(output)