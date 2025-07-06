from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MedicalRecordViewSet,
    PatientViewSet,
    AppointmentViewSet,
    LabTestViewSet,
    LabResultViewSet,
    PrescriptionViewSet
)

# The router automatically generates URL patterns for our ViewSets
router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'labtests', LabTestViewSet)
router.register(r'labresults', LabResultViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'medicalrecords', MedicalRecordViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
