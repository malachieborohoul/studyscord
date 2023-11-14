from django.shortcuts import render

# Create your views here.
rooms =[
    {'id':1, 'name': "Learn python"},
    {'id':2, 'name': "Javascript in action"},
    {'id':3, 'name': "Frontend devs"},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html' )