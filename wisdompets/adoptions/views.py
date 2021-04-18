from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>Home View</p>')

def pet_detail(request, pet_id):
    return HttpResponse(f'<p>pet_detail view for {pet_id}</p>')
