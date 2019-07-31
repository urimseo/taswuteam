from django.shortcuts import render
from .models import Taswu
# Create your views here.
def home(request):
    return render(request, 'home.html')

def taxi(request):
    return render (request, 'taxi.html')  

def car(request):
    return render(request, 'car.html')  

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request,'signup.html')

def mypage(request):
    return render(request, 'mypage.html')

def extra(request):
    return render(request,'extra.html')

def hwarang(request):
    Taswus = Taswu.objects
    return render(request, 'hwarang.html', {'Taswus' : Taswus})

def taereung(request):
    Taswus = Taswu.objects
    return render(request, 'taereung.html', {'Taswus' : Taswus})

def seokgye(request):
    Taswus = Taswu.objects
    return render(request, 'seokgye.html', {'Taswus' : Taswus})
