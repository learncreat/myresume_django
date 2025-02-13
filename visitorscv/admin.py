from django.contrib import admin

# Register your models here.
from .models import Resume, LoginAttempt, ResumeView

admin.site.register(Resume)
admin.site.register(LoginAttempt)
admin.site.register(ResumeView)

# Improvement I
from .models import PersonalData, ProfessionalExperience, Education, Skill, LoginAttempt, ResumeView

admin.site.register(PersonalData)
admin.site.register(ProfessionalExperience)
admin.site.register(Education)
admin.site.register(Skill)
