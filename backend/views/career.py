from rest_framework.viewsets import ModelViewSet
from backend.models import CareerFormSubmission
from backend.serializers.career import CareerFormSubmissionSerializer
from backend.permissions import ContactFormPermission
class CareerFormViewSet(ModelViewSet):
    queryset = CareerFormSubmission.objects.all()
    serializer_class = CareerFormSubmissionSerializer
    permission_classes = [ContactFormPermission]