from django.urls import path, include
# from drf_spectacular.view import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import TaskViewSet
router: ExtendedSimpleRouter = ExtendedSimpleRouter()
router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
