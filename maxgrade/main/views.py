from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def registration(request):
    return render(request, 'registration/login.html')

def shop(request):
    return render(request, 'shop/list.html')

