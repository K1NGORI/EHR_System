from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# NEW MODEL to store vitals, diagnosis, etc.
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    vitals = models.JSONField(null=True, blank=True) # For height, weight, BP
    diagnosis = models.TextField(blank=True)
    symptoms = models.TextField(blank=True)
    notes = models.TextField(blank=True)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)

class LabTest(models.Model):
    test_name = models.CharField(max_length=100)
    test_code = models.CharField(max_length=50)
    description = models.TextField()

class LabResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='lab_results')
    test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    result_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    # UPDATED: Add a field for the actual results
    result_data = models.TextField(blank=True) # To store the outcome
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE) # To know which doctor/nurse requested it

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prescriptions_written')
    pharmacist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='prescriptions_dispensed')
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100) # Added from class diagram
    frequency = models.CharField(max_length=100) # Added from class diagram
    created_date = models.DateTimeField(auto_now_add=True)
    # UPDATED: Add a status field
    status = models.CharField(max_length=20, default='Prescribed') # e.g., 'Prescribed', 'Dispensed'
