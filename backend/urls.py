from rest_framework.routers import DefaultRouter
from django.urls import path, include
from backend.views.contact import ContactViewSet
from backend.views.career import CareerFormViewSet


router = DefaultRouter()
router.register(r"contact", ContactViewSet, basename="contact")
router.register(r"career", CareerFormViewSet, basename="career")


urlpatterns = router.urls