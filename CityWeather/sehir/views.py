from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests

def index(request):
    populer_sehirler = ['Istanbul', 'Ankara', 'Izmir']
    return render(request, 'sehir/index.html', {'populer_sehirler': populer_sehirler})

def sehir_detay(request, isim):
    api_key = 'YOUR_OPENWEATHER_API_KEY'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={isim}&appid={api_key}&units=metric&lang=tr'
    response = requests.get(url)
    hava = response.json() if response.status_code == 200 else None
    return render(request, 'sehir/sehir_detay.html', {'hava': hava})

@login_required
def favoriler(request):
    # burada favori şehirleri db'den çekebiliriz
    favori_sehirler = []  # şimdilik boş
    return render(request, 'sehir/favoriler.html', {'favori_sehirler': favori_sehirler})

def hakkinda(request):
    return render(request, 'sehir/hakkinda.html')

