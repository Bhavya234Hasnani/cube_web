from rest_framework import ModelViewSet
from backend.models import ContactFormSubmission
from backend.serializers import ContactFormSubmissionSerializer
from backend.permissions import ContactFormPermission

class ContactViewSet(ModelViewSet):
    queryset = ContactFormSubmission.objects.all()
    serializer_class = ContactFormSubmissionSerializer
    permission_classes = [ContactFormPermission]

    