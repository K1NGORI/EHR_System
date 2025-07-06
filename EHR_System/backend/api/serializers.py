from rest_framework import serializers
from .models import MedicalRecord, Patient, Appointment, LabTest, LabResult, Prescription
from django.contrib.auth.models import User

# Serializer for the built-in User model (for Doctors, Pharmacists, etc.)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

# Serializer for the Patient model
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

# Serializer for the Appointment model
class AppointmentSerializer(serializers.ModelSerializer):
    # We use nested serializers to show details of the patient and doctor
    patient = PatientSerializer(read_only=True)
    doctor = UserSerializer(read_only=True)
    
    # These fields are for creating/updating appointments using IDs
    patient_id = serializers.IntegerField(write_only=True)
    doctor_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'appointment_date', 'status', 'created_date', 'patient_id', 'doctor_id']

# Serializer for LabTest model
class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = '__all__'

# Serializer for LabResult model
class LabResultSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    test = LabTestSerializer(read_only=True)
    
    patient_id = serializers.IntegerField(write_only=True)
    test_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = LabResult
        fields = ['id', 'patient', 'test', 'result_date', 'status', 'patient_id', 'test_id']

# Serializer for Prescription model
class PrescriptionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = UserSerializer(read_only=True)
    pharmacist = UserSerializer(read_only=True, allow_null=True)

    patient_id = serializers.IntegerField(write_only=True)
    doctor_id = serializers.IntegerField(write_only=True)
    pharmacist_id = serializers.IntegerField(write_only=True, allow_null=True)
    
    class Meta:
        model = Prescription
        fields = ['id', 'patient', 'doctor', 'pharmacist', 'medication_name', 'created_date', 'patient_id', 'doctor_id', 'pharmacist_id']
    
class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    patient_id = serializers.IntegerField(write_only=True)
    created_by_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MedicalRecord
        fields = '__all__'
