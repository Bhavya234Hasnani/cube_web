from rest_framework.serializers import ModelSerializer
from backend.models import ContactFormSubmission

class ContactFormSubmissionSerializer(ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = "__all__"


    
