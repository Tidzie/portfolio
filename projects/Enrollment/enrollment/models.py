from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_full_name()}"

class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Enrollment(models.Model):
    CLASS_TYPES = [
        ('FULL_DAY', 'Full Day'),
        ('HALF_DAY', 'Half Day'),
        ('EXTENDED_DAY', 'Extended Day'),
    ]

    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField()
    class_type = models.CharField(max_length=20, choices=CLASS_TYPES)
    status = models.CharField(max_length=20, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.child} - {self.class_type} - {self.enrollment_date}"
