from django.db import models
from django.contrib.auth.models import User
from django.db.models import Manager

# Create your models here.

class Company(models.Model):
    objects: Manager = models.Manager()

    EMPLOYEE_CHOICES = [
        ('<10', 'Less than 10'),
        ('10-50', '10 to 50'),
        ('50-150', '50 to 150'),
        ('150-300', '150 to 300'),
        ('300-500', '300 to 500'),
        ('500+', '500+'),
    ]

    TURNOVER_CHOICES = [
        ('<1L', 'Less than Rs.1L'),
        ('1L-10L', 'Rs. 1L to Rs. 10L'),
        ('10L-50L', 'Rs. 10L to Rs. 50L'),
        ('50L-100L', 'Rs. 50L to Rs. 100L'),
        ('100L+', 'More than Rs. 100L'),
    ]

    INDUSTRY_CHOICES = [
        ('IT', 'Information Technology'),
        ('MANUFACTURING', 'Manufacturing'),
        ('RETAIL', 'Retail'),
        ('HEALTHCARE', 'Healthcare'),
        ('FINANCE', 'Finance'),
        ('EDUCATION', 'Education'),
        ('OTHER', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_url = models.URLField(max_length=200)
    headquarters_location = models.CharField(max_length=200)
    company_email = models.EmailField()
    number_of_employees = models.CharField(max_length=20, choices=EMPLOYEE_CHOICES)
    turnover = models.CharField(max_length=20, choices=TURNOVER_CHOICES)
    industry_type = models.CharField(max_length=20, choices=INDUSTRY_CHOICES)
    company_description = models.TextField()
    year_established = models.PositiveIntegerField()
    registration_number = models.CharField(max_length=100)
    contact_person_name = models.CharField(max_length=100)
    contact_person_position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    social_media_linkedin = models.URLField(blank=True)
    social_media_twitter = models.URLField(blank=True)
    is_profile_completed = models.BooleanField(default=False)  # type: ignore
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
