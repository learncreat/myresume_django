# from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    title = models.CharField(max_length=100, default="Jorge's Resume")
    resume_file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.title


class LoginAttempt(models.Model):
    # If a valid user is associated, store it; otherwise, null.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email_entered = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        status = 'Success' if self.successful else 'Failed'
        return f"{self.email_entered} at {self.timestamp} - {status}"


class ResumeView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} viewed at {self.timestamp}"

# New Models for Resume Content

# 1. Personal Data (Static – only one record is expected)
class PersonalData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    nationality = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    profile_photo = models.ImageField(upload_to='profile_photos/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# 2. Professional Experience (Dynamic – supports multiple entries)
class ProfessionalExperience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    company_sector = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} at {self.company}"


# 3. Education (Dynamic – supports multiple entries)
class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.institution}"


# 4. Skills (Dynamic – supports multiple entries)
class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title