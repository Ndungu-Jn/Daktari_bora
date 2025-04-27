from django.db import models
from django.contrib.auth.models import User
from programs.models import Program

class Client(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_address(self):
        address_parts = [part for part in [self.street_address, self.city, self.state, self.zip_code] if part]
        return ", ".join(address_parts) if address_parts else "No address provided"

class ClientProgram(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('discontinued', 'Discontinued'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='programs')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    
    class Meta:
        unique_together = ('client', 'program')
    
    def __str__(self):
        return f"{self.client} - {self.program} ({self.status})"