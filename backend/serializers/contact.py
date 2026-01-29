from rest_framework import serializers

class ContactSubmissionSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=100)
    phone = serializers.CharField(required=True,max_length=10)
    email = serializers.EmailField(required=True)
    message = serializers.CharField(required=True)

