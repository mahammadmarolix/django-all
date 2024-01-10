from django.db import models

# Create your models here.


class job_details(models.Model):
    Qualification = models.CharField(max_length=150)
    required_skills = models.CharField(max_length=150)
    experiences_required = models.CharField(max_length=30)
    vacancies = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    application_deadline = models.CharField(max_length=150)