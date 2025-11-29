# sehir/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    sehirler = ['Izmir', 'Istanbul', 'Ankara', 'Bursa', 'Antalya']
    return render(request, 'sehir/index.html', {'sehirler': sehirler})

def sehir_detay(request, sehir_adi):
    sehirler = {
        'Izmir': {'name': 'İzmir', 'temp': 22, 'desc': 'Güneşli'},
        'Istanbul': {'name': 'İstanbul', 'temp': 18, 'desc': 'Bulutlu'},
        'Ankara': {'name': 'Ankara', 'temp': 15, 'desc': 'Yağmurlu'},
        'Bursa': {'name': 'Bursa', 'temp': 20, 'desc': 'Parçalı Bulutlu'},
        'Antalya': {'name': 'Antalya', 'temp': 25, 'desc': 'Güneşli'},
    }
    hava = sehirler.get(sehir_adi)
    return render(request, 'sehir/sehir_detay.html', {'hava': hava})

@login_required
def favoriler(request):
    favori_sehirler = []  # boş örnek
    return render(request, 'sehir/favoriler.html', {'favori_sehirler': favori_sehirler})

def hakkinda(request):
    return render(request, 'sehir/hakkinda.html')
