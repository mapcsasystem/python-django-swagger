from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/',
         SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger'),
    path('auth/user/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('auth/user/refresh-token/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/user/veriry-token/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include('apps.task.urls'), name='task'),
]
