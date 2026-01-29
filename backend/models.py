from django.db import models

# Create your models here.
class ContactFormSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.TextField()
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("closed", "Closed")
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="new")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.status})"
    
class CareerFormSubmission(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)#by default its blankk only
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    DOB = models.DateField()
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    permanent_address = models.TextField()
    current_address = models.TextField()
    experience = models.PositiveIntegerField()
    tech_stack = models.CharField(max_length=100)
    NOTICE_CHOICES = [
        ("Immediate","immediate"),
        ("Days","days"),
        ("Weeks","weeks")
    ]
    notice_period_type = models.CharField(choices=NOTICE_CHOICES, max_length=10)
    notice_period_value = models.PositiveIntegerField(null=True, blank=True,)
    RELOCATION_CHOICES = [
        ("yes", "Yes"),
        ("no", "No")
    ]
    able_to_relocate = models.CharField(max_length=3, choices=RELOCATION_CHOICES)
    interview_date = models.DateField()
    current_salary = models.PositiveIntegerField()
    expected_salary = models.PositiveIntegerField()
    current_company = models.CharField(max_length=200)
    resume = models.FileField(upload_to="resumes/",null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.tech_stack}"