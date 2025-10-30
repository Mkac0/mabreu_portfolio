from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('project/<slug:slug>/', views.project_detail, name='project_detail'), 
    path('resume/', views.resume, name='resume'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
