# from django.conf.urls import url
from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"user", UserProfileViewSet)
router.register(r"order", OrderViewSet, basename="order")


urlpatterns = [
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

              ] + router.urls
