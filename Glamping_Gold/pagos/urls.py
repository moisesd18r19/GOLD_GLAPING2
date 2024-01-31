from . import views
from django.urls import path

urlpatterns = [      
    path('', views.pagos, name='pagos'),   
    path('pago_status_/<int:pago_id>/', views.change_status_author, name='pago_status'),            
    path('create/', views.create_pago, name='create_pago'),   
    path('detail/<int:pago_id>/', views.detail_pago, name='detail_pago'), 
    path('delete/<int:pago_id>/', views.delete_pago, name='delete_pago'),   
]