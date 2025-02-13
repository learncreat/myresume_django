from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.custom_login, name='login'),
    path('resume/', views.resume_view, name='resume'),
    path('experience-filter/', views.experience_filter_view, name='experience_filter'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Dashboard view (see below)
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]