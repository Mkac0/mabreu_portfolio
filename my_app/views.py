from django.shortcuts import render
from .models import Project

def home(request):
    featured_projects = Project.objects.filter(is_featured=True).order_by('-date_completed')
    context = {
        'page_title': 'Developer Portfolio - Home',
        'projects': featured_projects,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    return render(request, 'about.html')

def resume(request):
    context = {
        'page_title': 'My Resume'
    }
    return render(request, 'resume.html', context)

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')
