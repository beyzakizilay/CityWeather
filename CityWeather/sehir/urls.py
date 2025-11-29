from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sehir/<str:isim>/', views.sehir_detay, name='sehir_detay'),
    path('favoriler/', views.favoriler, name='favoriler'),
    path('hakkinda/', views.hakkinda, name='hakkinda'),
    path('<str:sehir_adi>/', views.sehir_detay, name='sehir_detay'),
    path('', views.index, name='index'),  # Ana sayfa
    path('<str:sehir_adi>/', views.sehir_detay, name='sehir_detay'),  # Şehir detayları

]

