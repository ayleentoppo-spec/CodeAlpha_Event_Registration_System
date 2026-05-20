from django.urls import path
from . import views
urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('registrations/', views.my_registrations, name='my_registrations'),
    path('registrations/<int:pk>/cancel/', views.cancel_registration, name='cancel_registration'),
]
