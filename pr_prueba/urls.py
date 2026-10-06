from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sumar.urls')), # Esto hace que la calculadora sea la página de inicio
]