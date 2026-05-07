from django.shortcuts import render
from .models import Profile, Project, Experience, Skill, ProjectCategory, Certificate

def index(request):
    # Fetch data from the database
    categories = ProjectCategory.objects.all().prefetch_related('projects')
    experiences = Experience.objects.all()
    
    # Separate certificates and achievements
    certificates_list = Certificate.objects.filter(category='certificate')
    achievements_list = Certificate.objects.filter(category='achievement')
    
    # Organize skills by category
    skills = {
        'languages': Skill.objects.filter(category='Languages'),
        'ai_ml': Skill.objects.filter(category='AI_ML'),
        'data': Skill.objects.filter(category='Data'),
        'tools': Skill.objects.filter(category='Tools'),
    }
    
    context = {
        'categories': categories,
        'experiences': experiences,
        'skills': skills,
        'certificates_list': certificates_list,
        'achievements_list': achievements_list,
        'profile': Profile.objects.first(),
    }
    return render(request, 'main/index.html', context)
