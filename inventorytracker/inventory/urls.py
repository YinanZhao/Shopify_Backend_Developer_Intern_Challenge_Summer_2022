from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('locations/', views.modify_locations, name='locations'),
    path('<int:item_id>/detail/', views.detail, name='detail'),
    path('<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('<int:location_id>/delete_location/', views.delete_location, name='delete_location'),
]