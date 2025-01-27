from django.urls import path
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'bukutamu', api_views.BukuTamuViewSet)
router.register(r'members', api_views.MemberViewSet)

urlpatterns = router.urls 