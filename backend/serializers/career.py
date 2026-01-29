from rest_framework.serializers import ModelSerializer
from backend.models import CareerFormSubmission
from rest_framework import serializers

class CareerFormSubmissionSerializer(ModelSerializer):
    

    class Meta:
        model = CareerFormSubmission
        fields = "__all__"
    

    def validate(self,data):
        notice_period_type = data.get("notice_period_type")
        notice_period_value = data.get("notice_period_value")
        phone = data.get("phone")

        if not phone.isdigit():
            raise serializers.ValidationError("Phone number is not valid")
        
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        if not first_name.isalpha() or not last_name.isalpha():
            raise serializers.ValidationError("Name is not valid")
        


        if notice_period_type == "Days" or notice_period_type == "Weeks":
            if not notice_period_value:
                raise serializers.ValidationError("Notice period value is required")
            notice_period_value = serializers.IntegerField(required=True)
            
        else:
            notice_period_value = None

        return data
    resume = serializers.FileField(required=True)


    