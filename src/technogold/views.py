from django.shortcuts import render

def Home(request):
    return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')

def About(request):
    return render(request, 'about.html')

def Services(request):
    return render(request, 'services.html')