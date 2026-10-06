from django.urls import path
from . import views

urlpatterns = [
    path('', views.sumar_view, name='sumar'),
]