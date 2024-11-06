from django.urls import path
from . import views

urlpatterns = [
    path('api/set-address/', views.set_address, name='set_address'),
    path('api/addresses/', views.get_addresses, name='get_addresses'),
    path('api/address/<uuid:address_id>/', views.get_address_detail, name='get_address_detail'),
]
