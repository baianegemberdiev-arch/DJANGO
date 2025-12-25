from django.urls import path
from .views import car_list, bicycle_list

urlpatterns = [
    path('', car_list),
    path('bicycles/', bicycle_list),
]
