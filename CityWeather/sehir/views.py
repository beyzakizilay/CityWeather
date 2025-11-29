from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

def index(request):
    populer_sehirler = ['Istanbul', 'Ankara', 'Izmir']
    return render(request, 'sehir/index.html', {'populer_sehirler': populer_sehirler})

def sehir_detay(request, isim):
    api_key = 'YOUR_OPENWEATHER_API_KEY'  # kendi API anahtarını buraya koy
    url = f'https://api.openweathermap.org/data/2.5/weather?q={isim}&appid={api_key}&units=metric&lang=tr'
    try:
        response = requests.get(url)
        hava = response.json() if response.status_code == 200 else None
    except:
        hava = None
    return render(request, 'sehir/sehir_detay.html', {'hava': hava})

@login_required
def favoriler(request):
    favori_sehirler = []  # şimdilik boş
    return render(request, 'sehir/favoriler.html', {'favori_sehirler': favori_sehirler})

def hakkinda(request):
    return render(request, 'sehir/hakkinda.html')
from django.shortcuts import render

def sehir_detay(request, sehir_adi):
    sehirler = {
        'Izmir': {
            'name': 'İzmir',
            'main': {'temp': 22},
            'weather': [{'description': 'Güneşli'}],
        },
        'Istanbul': {
            'name': 'İstanbul',
            'main': {'temp': 18},
            'weather': [{'description': 'Bulutlu'}],
        },
        'Ankara': {
            'name': 'Ankara',
            'main': {'temp': 15},
            'weather': [{'description': 'Yağmurlu'}],
        },
        'Bursa': {
            'name': 'Bursa',
            'main': {'temp': 20},
            'weather': [{'description': 'Parçalı Bulutlu'}],
        },
        'Antalya': {
            'name': 'Antalya',
            'main': {'temp': 25},
            'weather': [{'description': 'Güneşli'}],
        },
        'Adana': {
            'name': 'Adana',
            'main': {'temp': 28},
            'weather': [{'description': 'Sıcak'}],
        },
        'Trabzon': {
            'name': 'Trabzon',
            'main': {'temp': 16},
            'weather': [{'description': 'Yağmurlu'}],
        },
        'Konya': {
            'name': 'Konya',
            'main': {'temp': 14},
            'weather': [{'description': 'Rüzgarlı'}],
        },
        'Mersin': {
            'name': 'Mersin',
            'main': {'temp': 27},
            'weather': [{'description': 'Güneşli'}],
        },
        'Eskişehir': {
            'name': 'Eskişehir',
            'main': {'temp': 17},
            'weather': [{'description': 'Bulutlu'}],
        },
    }

    hava = sehirler.get(sehir_adi)

    return render(request, 'sehir/sehir_detay.html', {'hava': hava})

def index(request):
    sehirler = [
        'Izmir', 'Istanbul', 'Ankara', 'Bursa', 'Antalya',
        'Adana', 'Trabzon', 'Konya', 'Mersin', 'Eskişehir'
    ]
    return render(request, 'sehir/index.html', {'sehirler': sehirler})
