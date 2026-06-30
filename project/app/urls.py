from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_request, name='add_request'),
    path('edit/<int:pk>/', views.edit_request_view, name='edit_request'),
    path('delete/<int:pk>/', views.delete_request_view, name='delete_request'),
]