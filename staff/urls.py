from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('update/<int:cid>/', views.update_status, name='update_status'),
]
