from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def merch(request):
    return render(request, 'merch.html') 