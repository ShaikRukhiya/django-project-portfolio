from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def education(request):
    return render(request, 'portfolio/education.html')

def project(request):
    return render(request, 'portfolio/project.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
