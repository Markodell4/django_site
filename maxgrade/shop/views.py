from django.shortcuts import render
from .models import Clothes

def shop_home(request):
    clothes = Clothes.objects.all()
    return render(request, 'shop/shop_home.html', {'shop': clothes})
