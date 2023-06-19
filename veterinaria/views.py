from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {})
