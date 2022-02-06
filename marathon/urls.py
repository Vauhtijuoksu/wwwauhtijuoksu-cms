from django.urls import path

from . import views

urlpatterns = [
    path('', views.active_event),
    path('<slug:event>/', views.event_detail),
    path('<slug:event>/submission/', views.new_submission),
]