from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    sehirler = [
        'Izmir', 'Istanbul', 'Ankara', 'Bursa', 'Antalya',
        'Adana', 'Trabzon', 'Konya', 'Mersin', 'Eskisehir'
    ]
    return render(request, 'sehir/index.html', {'sehirler': sehirler})

def sehir_detay(request, sehir_adi):
    sehirler = {
        'Izmir': {'name': 'İzmir', 'temp': 22, 'description': 'Güneşli'},
        'Istanbul': {'name': 'İstanbul', 'temp': 18, 'description': 'Bulutlu'},
        'Ankara': {'name': 'Ankara', 'temp': 15, 'description': 'Yağmurlu'},
        'Bursa': {'name': 'Bursa', 'temp': 20, 'description': 'Parçalı Bulutlu'},
        'Antalya': {'name': 'Antalya', 'temp': 25, 'description': 'Güneşli'},
        'Adana': {'name': 'Adana', 'temp': 28, 'description': 'Sıcak'},
        'Trabzon': {'name': 'Trabzon', 'temp': 16, 'description': 'Yağmurlu'},
        'Konya': {'name': 'Konya', 'temp': 14, 'description': 'Rüzgarlı'},
        'Mersin': {'name': 'Mersin', 'temp': 27, 'description': 'Güneşli'},
        'Eskisehir': {'name': 'Eskişehir', 'temp': 17, 'description': 'Bulutlu'},
    }

    hava = sehirler.get(sehir_adi)
    if not hava:
        return render(request, 'sehir/sehir_detay.html', {'error': 'Şehir bulunamadı!'})

    return render(request, 'sehir/sehir_detay.html', {'hava': hava})

@login_required
def favoriler(request):
    favori_sehirler = ['Izmir', 'Ankara']  # Örnek olarak favoriler
    return render(request, 'sehir/favoriler.html', {'favori_sehirler': favori_sehirler})

def hakkinda(request):
    return render(request, 'sehir/hakkinda.html')
