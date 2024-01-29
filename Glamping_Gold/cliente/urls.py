from . import views
from django.urls import path

urlpatterns = [      
    path('', views.cliente, name='cliente'),     
    path('cliente_status/<int:cliente_id>/', views.change_status_cliente, name='cliente_status'),  
    path('create/', views.create_cliente, name='create_cliente'),   
]