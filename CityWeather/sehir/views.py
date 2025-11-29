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
