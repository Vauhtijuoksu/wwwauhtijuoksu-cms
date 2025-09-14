from django.urls import path

from . import views

urlpatterns = [
    path('', views.active_event),
    path('<slug:event>/', views.event_detail),
    path('<slug:event>/submission/', views.new_submission, name='new-submission'),
    path('<slug:event>/edit/<slug:submission_id>', views.edit_submission, name='edit-submission'),
    path('thanks', views.thanks),
]