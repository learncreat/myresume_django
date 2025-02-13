# visitorscv/urls_api.py
from django.urls import path, include
from rest_framework import routers
from .api_views import PersonalDataViewSet, ProfessionalExperienceViewSet, EducationViewSet, SkillViewSet

router = routers.DefaultRouter()
router.register(r'personal-data', PersonalDataViewSet)
router.register(r'professional-experience', ProfessionalExperienceViewSet)
router.register(r'education', EducationViewSet)
router.register(r'skills', SkillViewSet)

urlpatterns = [
    path('', include(router.urls)),
]