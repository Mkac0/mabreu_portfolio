from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    featured_projects = Project.objects.filter(is_featured=True).order_by('-date_completed')
    context = {
        'page_title': 'Developer Portfolio - Home',
        'projects': featured_projects,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    return render(request, 'portfolio/about.html')

def resume(request):
    context = {
        'page_title': 'My Resume'
    }
    return render(request, 'portfolio/resume.html', context)

def projects(request):
    """Placeholder or a view to list all projects."""
    context = {
        'page_title': 'All Projects'
    }
    return render(request, 'portfolio/projects.html', context)

def project_detail(request, slug):
    """
    Fetches a single project based on its unique slug.
    """
    project = get_object_or_404(Project, slug=slug)
    context = {
        'page_title': project.title,
        'project': project,
    }
    return render(request, 'portfolio/project_detail.html', context)

def contact(request):
    return render(request, 'portfolio/contact.html')
