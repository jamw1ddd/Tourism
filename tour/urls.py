from django.urls import path
from .views import index, contact,region_detail, city_detail, place_detail, place_list

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('region/<int:pk>/', region_detail, name='region_detail'),
    path('city/<int:pk>/', city_detail, name='city_detail'),
    path('place/<int:pk>/', place_detail, name='place_detail'),
    path('place/', place_list, name='place'),
]
