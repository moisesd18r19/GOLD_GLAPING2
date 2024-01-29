from . import views
from django.urls import path

urlpatterns = [      
    path('', views.tipocabañas, name='tipocabañas'),
    path('tipocabaña_status_/<int:tipocabaña_id>/', views.change_status_tipocabaña, name='tipocabaña_status'), 
    path('create/', views.create_tipocabaña, name='create_tipocabaña'), 
    path('', views.tipocabañas, name='tipocabañas'),  
    
         
]            
