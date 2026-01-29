from rest_framework.serializers import ModelSerializer
from backend.models import ContactFormSubmission
from rest_framework import serializers

class ContactFormSubmissionSerializer(ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = "__all__"
    def validate(self,data):
        phone = data.get("phone")
        if not phone.isdigit():
            raise serializers.ValidationError("Phone number is not valid")
        first_name = data.get("first_name")
        last_name = data.get("last_name")   
        if not first_name.isalpha() or not last_name.isalpha():
            raise serializers.ValidationError("Name is not valid")

        return data



    
