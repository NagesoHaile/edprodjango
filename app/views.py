from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Member
# Create your views here.
from django.views.generic import ListView

class MemberListView(ListView):
    model = Member
    template_name = 'member_list.html'
    

