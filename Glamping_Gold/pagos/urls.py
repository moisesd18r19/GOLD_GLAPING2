from .import views
from django.urls import path

urlpatterns = [      
    path('', views.pagos, name='pagos'),   
    path('pago_status_/<int:pago_id>/', views.change_status_pago, name='pago_status'),            
    path('create/', views.create_pagos, name='create_pagos'),   
        
 ]