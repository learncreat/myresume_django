from rest_framework import viewsets
from .models import PersonalData, ProfessionalExperience, Education, Skill
from .serializers import PersonalDataSerializer, ProfessionalExperienceSerializer, EducationSerializer, SkillSerializer

class PersonalDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PersonalData.objects.all()
    serializer_class = PersonalDataSerializer

class ProfessionalExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProfessionalExperience.objects.all()
    serializer_class = ProfessionalExperienceSerializer

class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer