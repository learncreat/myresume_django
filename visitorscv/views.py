# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PersonalData, ProfessionalExperience, Education, Skill, LoginAttempt, ResumeView


def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        ip_address = request.META.get('REMOTE_ADDR')

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            username = None

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            LoginAttempt.objects.create(user=user, email_entered=email, successful=True, ip_address=ip_address)
            return redirect('resume')
        else:
            LoginAttempt.objects.create(email_entered=email, successful=False, ip_address=ip_address)
            messages.error(request, 'Invalid email or password.')
    return render(request, 'visitorscv/login.html')


@login_required
def resume_view(request):
    # Fetch the resume data from the database
    personal_data = PersonalData.objects.first()  # Assumes only one record exists
    professional_experiences = ProfessionalExperience.objects.all().order_by('-start_date')
    education_entries = Education.objects.all().order_by('-start_date')
    skills = Skill.objects.all()

    # Log the resume view
    ResumeView.objects.create(user=request.user)

    context = {
        'personal_data': personal_data,
        'professional_experiences': professional_experiences,
        'education_entries': education_entries,
        'skills': skills,
    }
    return render(request, 'visitorscv/resume.html', context)

# visitorscv/views.py (add this below your existing views)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ProfessionalExperience
from .filters import ProfessionalExperienceFilter

@login_required
def experience_filter_view(request):
    f = ProfessionalExperienceFilter(request.GET, queryset=ProfessionalExperience.objects.all())
    return render(request, 'visitorscv/experience_filter.html', {'filter': f})

# Improve II

import datetime
from django.db.models import Count
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from .models import LoginAttempt, ResumeView, ProfessionalExperience, Education, Skill

@staff_member_required
def dashboard_view(request):
    # Aggregate statistics
    total_login_attempts = LoginAttempt.objects.count()
    total_successful_logins = LoginAttempt.objects.filter(successful=True).count()
    total_failed_logins = LoginAttempt.objects.filter(successful=False).count()
    total_resume_views = ResumeView.objects.count()

    today = timezone.now().date()
    todays_resume_views = ResumeView.objects.filter(timestamp__date=today).count()

    # Counts for dynamic resume components
    total_experiences = ProfessionalExperience.objects.count()
    total_education = Education.objects.count()
    total_skills = Skill.objects.count()

    context = {
        'total_login_attempts': total_login_attempts,
        'total_successful_logins': total_successful_logins,
        'total_failed_logins': total_failed_logins,
        'total_resume_views': total_resume_views,
        'todays_resume_views': todays_resume_views,
        'total_experiences': total_experiences,
        'total_education': total_education,
        'total_skills': total_skills,
    }
    return render(request, 'visitorscv/dashboard.html', context)