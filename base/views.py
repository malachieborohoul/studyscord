from django.shortcuts import render

# Create your views here.
rooms =[
    {'id':1, 'name': "Learn python"}
]

def home(request):
    return render(request, 'base/home.html')

def room(request):
    return render(request, 'base/room.html' )