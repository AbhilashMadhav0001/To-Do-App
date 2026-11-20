from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('update/<int:id>/', views.update_todo, name='update'),
    
    path('delete/<int:id>/', views.delete_todo, name='delete'),
    
    path('complete/<int:id>/', views.complete, name='complete'),
    
]