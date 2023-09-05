from django.urls import path
from . import views

urlpatterns = [
    # URL patterns for the Member model
    path('members/', views.MemberListCreateView.as_view(), name='member-list'),
    path('members/<int:pk>/', views.MemberDetailView.as_view(), name='member-detail'),

    # Define similar URL patterns for other models (Admin, Event, Contribution, etc.)
    path('admins/', views.AdminListCreateView.as_view(), name='admin-list'),
    path('admins/<int:pk>/', views.AdminDetailView.as_view(), name='admin-detail'),
    
    # Repeat the process for each model's URL patterns
]
