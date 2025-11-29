from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sehir.urls')),        # ana sayfa ve şehirler
    path('accounts/', include('accounts.urls')),  # giriş/kayıt/çıkış
]
