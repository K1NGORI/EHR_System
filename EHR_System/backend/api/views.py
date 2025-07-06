from rest_framework import viewsets
from .models import MedicalRecord, Patient, Appointment, LabTest, LabResult, Prescription
from .serializers import (
    MedicalRecordSerializer,
    PatientSerializer, 
    AppointmentSerializer, 
    LabTestSerializer, 
    LabResultSerializer, 
    PrescriptionSerializer
)
class MedicalRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint for medical records (vitals, diagnosis).
    """
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    
    # Enable filtering by patient_id, e.g., /api/medicalrecords/?patient_id=1
    def get_queryset(self):
        queryset = MedicalRecord.objects.all()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset.order_by('-created_date')

    def perform_create(self, serializer):
        serializer.save(
            patient_id=self.request.data.get('patient_id'),
            created_by_id=self.request.data.get('created_by_id')
        )

class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    """
    queryset = Patient.objects.all().order_by('last_name')
    serializer_class = PatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for appointments.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    def perform_create(self, serializer):
        # When creating, link patient and doctor from their IDs
        serializer.save(
            patient_id=self.request.data.get('patient_id'),
            doctor_id=self.request.data.get('doctor_id')
        )

class LabTestViewSet(viewsets.ModelViewSet):
    """
    API endpoint for lab tests.
    """
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer

class LabResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint for lab results.
    """
    queryset = LabResult.objects.all()
    serializer_class = LabResultSerializer
    
    def perform_create(self, serializer):
        serializer.save(
            patient_id=self.request.data.get('patient_id'),
            test_id=self.request.data.get('test_id')
        )

class PrescriptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for prescriptions.
    """
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    
    def perform_create(self, serializer):
        serializer.save(
            patient_id=self.request.data.get('patient_id'),
            doctor_id=self.request.data.get('doctor_id')
        )