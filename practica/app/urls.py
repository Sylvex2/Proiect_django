from django.urls import path
from . import views

urlpatterns = [
    path('formular_bypass/', views.bypass, name='formular_bypass'),
    path('get-stations/<str:tip_statie>/', views.get_stations, name='get_stations'),
    path('get-station-details/<str:tip_statie>/<int:statie_id>/', views.get_station_details, name='get_station_details'),
    # alte rute...
]
