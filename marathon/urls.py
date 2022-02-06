from django.urls import path

from . import views

urlpatterns = [
    path('', views.active_event),
    path('events/<slug:slug>/', views.event_detail)
]