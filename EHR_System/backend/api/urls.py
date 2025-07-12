from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Import ALL your views, including the new one
from .views import (
    PatientViewSet,
    AppointmentViewSet,
    LabTestViewSet,
    LabResultViewSet,
    PrescriptionViewSet,
    MedicalRecordViewSet,
    CurrentUserView
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'labtests', LabTestViewSet)
router.register(r'labresults', LabResultViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'medicalrecords', MedicalRecordViewSet)

# This defines the URL for the new view
urlpatterns = [
    path('user/', CurrentUserView.as_view(), name='current-user'),
    path('', include(router.urls)),
]