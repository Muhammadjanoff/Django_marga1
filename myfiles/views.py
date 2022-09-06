from django.shortcuts import render

# Create your views here.

def index(malumot):
    return render(malumot,'index.html')

def about(malumot):
    return render(malumot,'about.html')

def blog(malumot):
    return render(malumot,'blog.html')

def project(malumot):
    return render(malumot,'project.html')

def services(malumot):
    return render(malumot,'services.html')

def contact(malumot):
    return render(malumot,'contact.html')