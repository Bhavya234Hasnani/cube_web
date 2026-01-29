from rest_framework.routers import DefaultRouter
from django.urls import path, include
from backend.views.contact import ContactViewSet

router = DefaultRouter()
router.register(r"contact", ContactViewSet, basename="contact")

urlpatterns = router.urls