from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Skill, Experience
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    featured_projects = Project.objects.filter(is_featured=True).order_by('-date_completed')
    context = {
        'page_title': 'Developer Portfolio - Home',
        'projects': featured_projects,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    """Fetches skills and displays them alongside about me content."""
    skills = Skill.objects.all().order_by('category', '-proficiency')
    categorized_skills = {}
    
    for skill in skills:
        category_name = skill.get_category_display()
        if category_name not in categorized_skills:
            categorized_skills[category_name] = []
        
        categorized_skills[category_name].append(skill)    
    context = {
        'page_title': 'About Me & Skills',
        'categorized_skills': categorized_skills,
    }
    return render(request, 'portfolio/about.html', context)

def resume(request):
    """Fetches and displays all professional experience."""
    work_experience = Experience.objects.all().order_by('-start_date')
    context = {
        'page_title': 'Work Experience & Résumé',
        'experiences': work_experience,
    }
    return render(request, 'portfolio/resume.html', context)

def projects(request):
    """Fetches and displays ALL projects."""
    all_projects = Project.objects.all().order_by('-date_completed')
    context = {
        'page_title': 'All My Projects',
        'all_projects': all_projects,
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
    """Handles the display and submission of the contact form."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            full_message = f"From: {name} <{email}>\n\nSubject: {subject}\n\nMessage:\n{message}"
            try:
                send_mail(
                    subject,
                    full_message,
                    email,
                    ['melissa.abreu84@gmail.com'],
                    fail_silently=False,
                )
                return redirect('home') 
            
            except Exception as e:
                print(f"Error sending email: {e}") 
                return render(request, 'portfolio/contact.html', {'form': form, 'page_title': 'Contact Me', 'error_message': 'Sorry, the email failed to send. Please try again or email me directly.'})
    else:
        form = ContactForm()

    context = {
        'page_title': 'Contact Me',
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)
