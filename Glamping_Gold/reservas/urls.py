from .import views
from django.urls import path


urlpatterns = [      
    path('', views.reservas, name='reservas'),
	path('reserva_status_/<int:reserva_id>/', views.change_status_reserva, name='reserva_status'),            
]