from django.urls import path
from .views import MemberListView

urlpatterns = [
    path('',MemberListView.as_view(), name='home'),
]
