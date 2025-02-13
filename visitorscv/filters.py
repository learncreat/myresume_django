# visitorscv/filters.py
import django_filters
from .models import ProfessionalExperience

class ProfessionalExperienceFilter(django_filters.FilterSet):
    # Filter experiences starting on or after a given date
    start_date = django_filters.DateFilter(field_name='start_date', lookup_expr='gte')
    # Filter experiences ending on or before a given date
    end_date = django_filters.DateFilter(field_name='end_date', lookup_expr='lte')
    # Case-insensitive search for the company name
    company = django_filters.CharFilter(field_name='company', lookup_expr='icontains')
    # Filter by employment type (e.g., Full-Time, Part-Time)
    employment_type = django_filters.CharFilter(field_name='employment_type', lookup_expr='icontains')

    class Meta:
        model = ProfessionalExperience
        fields = ['start_date', 'end_date', 'company', 'employment_type']