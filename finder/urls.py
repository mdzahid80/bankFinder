from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_data, name='search_data'),
]
