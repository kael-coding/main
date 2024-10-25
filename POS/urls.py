from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_items/', views.add_items, name='add_items'),
    path('views/', views.item_views, name='views'),
    path('purchase/', views.purchase, name='purchase'),
]